import requests
import unidecode
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from actors.models import Actor, ActorsMovie
from movies.models import Movie

BASE_URL = "https://www.csfd.cz"


class Command(BaseCommand):
    help = 'Get top movies and actors'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=300, type=int)

    def handle(self, *args, **options):
        try:

            self.stdout.write(self.style.SUCCESS('Script will extract  "%s" movies' % options['count']))
            cnt = 1
            for page_num in range(0, options['count'], 100):
                move_page = requests.get(f"https://www.csfd.cz/zebricky/filmy/nejlepsi/?from={page_num}",
                                         headers={'User-agent': 'your bot 0.1'})
                move_soup = BeautifulSoup(move_page.content, 'html.parser')
                try:
                    for link in move_soup.select('.film-title-name'):
                        if cnt == options['count']:
                            break
                        cnt += 1
                        movie, created = Movie.objects.get_or_create(
                            name=link['title'],
                            search_name=unidecode.unidecode(link['title']),
                            link=link['href'],
                        )
                        if created:
                            page_with_actors = requests.get(f"{BASE_URL}{link['href']}",
                                                            headers={'User-agent': 'your bot 0.1'})
                            page_with_actors_soup = BeautifulSoup(page_with_actors.content, 'html.parser')
                            try:
                                for div_sec in page_with_actors_soup.select('.creators div'):
                                    if "Hrají:" in div_sec.get_text():  # actors section
                                        for actor_html in div_sec.select('a'):
                                            if actor_html['href'] != "#":
                                                actor, created = Actor.objects.get_or_create(
                                                    full_name=actor_html.get_text(),
                                                    search_full_name=unidecode.unidecode(actor_html.get_text()),
                                                    link=actor_html['href'],
                                                )
                                                obj, created = ActorsMovie.objects.get_or_create(
                                                    actor=actor,
                                                    movie=movie,
                                                )
                            except BaseException as e:
                                self.stdout.write(f"Error in scraping actors {link['title']}. More info: {e}")
                except BaseException as e:
                    self.stdout.write(f"Error in scraping movie in page {page_num}. More info: {e}")
            self.stdout.write(self.style.SUCCESS(f'DONE {cnt} movies'))

        except BaseException as e:
            self.stdout.write(f"Error in scraping data. More info: {e}")

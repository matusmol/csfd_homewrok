# Generated by Django 3.2.13 on 2022-05-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('search_name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=400)),
            ],
        ),
    ]

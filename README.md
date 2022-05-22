# CSFD extractor

Program what load movies and their actors  
Simple searching  

## Setup
```
# creating virtual enviroment
python3.7 -m venv .venv

# activate virtual enviroment
source venv/bin/activate

# install packages
pip install -r requirements.txt

#init database
python manage.py migrate

# get data, by default will get 300 movies
python manage.py scraper_data

# optionally you can change your limit with additional movie limit (for example only 30 movies)
python manage.py scraper_data 30

# run server
python manage.py runserver
```


## USAGE
In your browser open http://127.0.0.1:8000/  
In the input field choose what movie or actor are you looking and after
 pressing Submit you will get a list with your match  
 Every row in result is link to info  
 In info pages you have links to all movies where actor plays or all actors who plays in this movie
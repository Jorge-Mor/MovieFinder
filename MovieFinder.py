import requests, json
from pprint import pprint
from flask import Flask,render_template, flash, redirect
from flask_bootstrap import Bootstrap5
import random
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


# create an instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'

#Create Bootstrap object (after Flask object):
bootstrap = Bootstrap5(app)

#class for playlist
class Playlist(FlaskForm):
  song_title = StringField(
    'Movie Title', 
    validators=[DataRequired()]
  )

#geting Api call
def themoviedbAPI(movie):
  my_key = '933dcbef063eeaeab80f38d6e792311c'
  apiLink = 'https://api.themoviedb.org/3/search/movie?api_key='+my_key+'&query='+movie


#api call return the posterLinks
def callApi():
  # This is a comment
  my_key = 'bcc4d5b1'
  apiLink = ' http://www.omdbapi.com/?s=' + getTitle() + '&apikey=bcc4d5b1'


  try:
    r = requests.get(apiLink)
    data = r.json()
    # pprint(data)

  except:
    print('please try again')
  return data

#Assigning movie names to background to get random colors and image on the home screen
movieNames = ['avenger', 'thing', 'black', 'wave', 'it', 'teen', 'john', 'the', 'him', 'one', 'hero']
background =['secondary', 'success','warning','info','primary','danger']
movieInformation = []


def store_song(movie):
  movieI = themoviedbAPI(movie)
  movieInformation.append(movieI)

#home page
@app.route('/', methods=('GET', 'POST'))
def index():
  #Collecting info from the home page and rendering to a new page if the search button is clicked
  form = Playlist()
  if form.validate_on_submit():
    movieInformation = []
    store_song(form.song_title.data)
    return redirect('/movie')

  data=themoviedbAPI(random.choice(movieNames))
  random_number = random.randint(0, 6)
  random_color = random.randint(0, 5)
  return render_template('index.html', form=form, my_data=data,random_number=random_number,background=background,random_color=random_color)
=======
def posterLinks(data):
  posterLinks = []
  for movie in data['Search']:
    print(movie['Title'], movie['Year'])
    posterLinks.append(movie['Poster'])
  return posterLinks



# https://api.themoviedb.org/3/search/movie?api_key=933dcbef063eeaeab80f38d6e792311c&query=Life
def themoviedbAPI(movie):
  my_key = '933dcbef063eeaeab80f38d6e792311c'
  apiLink = 'https://api.themoviedb.org/3/search/movie?api_key='+my_key+'&query='+movie


  try:
    r = requests.get(apiLink)
    data = r.json()
    # pprint(data)

  except:
    print('please try again')
  return data

movieNames = ['inception', 'thing', 'afterlife', 'wave']


# route decorator binds a function to a URL
# @app.route('/')
# def hello():
#   data=themoviedbAPI()
#   random_number = random.randint(0, 10)
#   pprint(data)
#   return render_template('index.html',my_data=data,random_number=random_number)


class Playlist(FlaskForm):
  song_title = StringField(
    'Movie Title', 
    validators=[DataRequired()]
  )


movieNames = ['avenger', 'thing', 'black', 'wave', 'it', 'teen', 'john', 'the', 'him', 'one', 'hero']
movieInformation = []
def store_song(movie):
  movieI = themoviedbAPI(movie)
  movieInformation.append(movieI)


@app.route('/', methods=('GET', 'POST'))
def index():
  form = Playlist()
  if form.validate_on_submit():
    movieInformation = []
    store_song(form.song_title.data)
    return redirect('/movie')

  data=themoviedbAPI(random.choice(movieNames))
  random_number = random.randint(0, 10)
  # pprint(data)
  return render_template('index.html', form=form, my_data=data,random_number=random_number)


@app.route('/movie')
def movie():
  return render_template('index2.html', movieInfo=movieInformation)




#movie page
@app.route('/movie')
def movie():
  return render_template('index2.html', movieInfo=movieInformation)
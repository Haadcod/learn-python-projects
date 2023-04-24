import flask
from flask import request,jsonify

app=flask.Flask(__name__)
app.config['DEBUG']=True
#create some test data for our catalogue inform of a list of dictionaries
books=[
    {'id':0,
     'title':'A fire upon the deep',
     'author':'venor vinge',
     'first_sentence':'The coldsleep itsself was dreamless.',
     'year_published':'1992'},
    {'id':1,
     'title':'The ones who walk away from omelas',
     'author':'ursula k .le Guin',
     'first_sentence':'With a clamor of bells the set the swallows swelling,the festival of the summer came to the city omelus,bright_towered by the sea',
     'year_published':'1973'},
    {'id':2,
     'title':'DhalGren',
     'author':'samuel R Delany',
     'first_sentence':'to wound the autumnal city',
     'year_published':'1975'}
]
@app.route('/',method=['GET'])
def home():
    return '''<h1>Distant Achieve</h1>
    <p1>A prototype API for distsnt reading of science iction novels'''
#A route to return all the available entries in our catalouge
@app.route('/api1/books/all',method=['GET'])
def ap1():
    return jsonify(books)
app.run()

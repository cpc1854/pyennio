import urllib
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

def get_webpage(url):
    #html = myHtml.get_webpage(url)
    req = urllib.request.Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req).read()

@app.route('/')
def index():
    return 'Ennio Python API'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/getrss')
def getrss():
    url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    url = 'https://www.google.com/alerts/feeds/17693298356275254038/2632410756866989756'
    xml = get_webpage(url)
    return xml


'''
@app.route('/')
def index():
    return render_template(
        'indexh.html',**locals())
'''
##def hello_world():
##  return 'Hey its Python Flask application on Azure!'
if __name__ == '__main__':
  app.run()

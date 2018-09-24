import urllib
from bs4 import BeautifulSoup
import sys
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort

import mylib
import pr_weblinks


app = Flask(__name__)


@app.route('/')
def index():
    return 'Ennio Python API'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/version')
def version():
    return sys.version

@app.route('/rss/')
def rss():
    #url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    #url = 'https://www.google.com/alerts/feeds/17693298356275254038/2632410756866989756'
    #if u == None: u = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    #u = 'sdafsdf'
    u =  request.args.get('u','http://feeds.bbci.co.uk/news/world/rss.xml')
    xml = mylib.get_webpage(u)
    return xml

@app.route('/weblinks/')
def weblinks():
    u =  request.args.get('u','https://edition.cnn.com/specials/cnn-heroes')    
    name =  request.args.get('name','cnn-heroes')        
    inurls =  request.args.get('inurls','cnnheroes,html')    
    not_inurls =  request.args.get('not_inurls','fag')    
    intitles =  request.args.get('intitles','')    
    not_intitles =  request.args.get('not_intitles','')    
    result = pr_weblinks.do_parsing(u, name, inurls, not_inurls, intitles, not_intitles)
   
    return result

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

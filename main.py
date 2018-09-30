import urllib
import json
from bs4 import BeautifulSoup
import sys
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort

'''
testing: 
    http://127.0.0.1:5000/
youtube_search:
    https://pyennio.azurewebsites.net/youtube_search/?q=cnn%2Bheroes
weblinks:
    https://pyennio.azurewebsites.net/weblinks/?name=cnn-heroes&u=https://edition.cnn.com/specials/cnn-heroes&inurls=cnnheroes,html&not_inurls=fag
alerts:    
    https://pyennio.azurewebsites.net/alerts/2418355790508839210    
'''

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

@app.route('/youtube_search/')
def youtube_search():
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&publishedAfter=2018-02-12T00:00:00Z&q={0}&key=AIzaSyAKw-hbjHCj_JXWRoZVd9eVPiTmElBPxX0'
    q =  request.args.get('q','cnn+heroes')
    url = url.format(q)
    xml = mylib.get_webpage(url)
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

@app.route('/alerts/<id>', defaults={'uid': '17693298356275254038'})    
@app.route('/alerts/<id>/<uid>')
def alerts(id,uid):
    #http://127.0.0.1:5000/alerts/2418355790508839210
    #https://pyennio.azurewebsites.net/alerts/17693298356275254038/2418355790508839210
    '''
    https://pyennio.azurewebsites.net/alerts/2418355790508839210
    '''
    u = 'https://www.google.com/alerts/feeds/{0}/{1}'.format(uid,id)
    xml = mylib.get_webpage(u)
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

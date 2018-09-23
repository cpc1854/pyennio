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

@app.route('/rss/')
def rss():
    #url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    #url = 'https://www.google.com/alerts/feeds/17693298356275254038/2632410756866989756'
    #if u == None: u = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    #u = 'sdafsdf'
    u =  request.args.get('u','http://feeds.bbci.co.uk/news/world/rss.xml')
    xml = get_webpage(u)
    return xml
    
@app.route('/alerts/<uid>/<aid>')
def alerts(uid,aid):
    #http://127.0.0.1:5000/alerts/17693298356275254038/2418355790508839210
    #uid =  request.args.get('uid', '')
    #aid =  request.args.get('aid', '')    
    u = 'https://www.google.com/alerts/feeds/{0}/{1}'.format(uid,aid)
    xml = get_webpage(u)
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

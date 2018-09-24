import urllib
from bs4 import BeautifulSoup
import sys
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort

import mylib
#import pr_weblinks

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

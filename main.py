from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'indexh.html',**locals())
##def hello_world():
##  return 'Hey its Python Flask application on Azure!'
if __name__ == '__main__':
  app.run()

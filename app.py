from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return 'Welcome to home'

@app.errorhandler(404)
def page_not_found(e):
    return 'sorry, page does not exist', 400
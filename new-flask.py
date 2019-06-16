from flask import Flask #importing a Class
app = Flask(__name__)   #creating an instance of the class

@app.route('/')  #decorator - injects special capabilities into our function, allowing that the code be assoc. with an endpoint.
def hello_world():   #"/" this is the root endpoint (beginning of the page)
    return 'Hello, World!'

@app.route('/wearehere')  #additional endpoint, add "/wearehere" on the running page and you get diff page.
def where_are_we():
    return "The web is cool and we are in it"

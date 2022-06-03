# This will import class Flask , and render_templete , url_for 
from flask import Flask, render_template,url_for


app = Flask(__name__)

# PAGES will show the output based on title and sources for html files according to the routes given
PAGES = [
    {'name':'Home', 'source':'home'},
    {'name':'About', 'source':'about'},
    {'name':'Project', 'source':'project'}
    ]


# '/' route will show up the initial page namely home
@app.route('/')
def home():
    return render_template('home.html', title='Home', pages=PAGES)

# '/about' route will navigate to about page by returning the rendered templete for about.html
@app.route('/about')
def about():
    return render_template('about.html', title='About', pages=PAGES)

# '/project' route will navigate the page and show up the details asked for projects 
@app.route('/project')
def project():
    return render_template('project.html', title='Project', pages=PAGES)
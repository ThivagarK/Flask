## render_template is responsible for redirecting to HTML webpage.
from flask import Flask,render_template

# WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    ## this is a HTML tag.
    return "<html><H1>Welcome to the Flask course</H1></html>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/index")
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
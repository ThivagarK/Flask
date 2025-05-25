## render_template is responsible for redirecting to HTML webpage.
from flask import Flask,render_template,request

# WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    ## this is a HTML tag.
    return "<html><H1>Welcome to the Flask course.</H1>" \
    "<p>This is a simple web application built in Flask.</p></html>"

@app.route('/about')
def about():
    return 'render_template'

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/form", methods=["GET","POST"])
def form():
    ## this condition works when clicking submit in the form.
    if request.method=='POST':
        ## text information id in the html file.
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

## this is executed once the action in the form template.
@app.route("/submit", methods=["GET","POST"])
def submit():
    ## this condition works when clicking submit in the form.
    if request.method=='POST':
        ## text information id in the html file.
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)
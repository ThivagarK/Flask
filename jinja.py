## Building URL Dynamically
## Jinja 2 template

## render_template is responsible for redirecting to HTML webpage.
## redirect is used in the Flask class to send user to a particular URL with status code.
## url_for is avoid changing URL has hard code based on applications.
from flask import Flask,render_template,request,redirect,url_for

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

## action tag in form.html
## route from the /form
@app.route('/success', methods=["GET","POST"])
def success():
    if request.method=='POST':
## this is attribute of label called name.
        name=request.form['score']
## typecast to display the value.
    return 'The mark I got is '+str(name)+'.'

## Jinja 2 template
## Jinja 2 template engine (methods to write datasource)
'''
{{}} expressions to print output in html
{%...%} conditional statement, example: for loops,while
{#...#} this is for comments
'''
## single output
## variable rule
@app.route('/marks/<int:score>')
def marks(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    return render_template('result.html',results=res)

## a data source as dictionary
## for loop condition
@app.route('/marks_res/<int:score>')
def marksres(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"

    exp={"scores":score,"results":res}
    return render_template('datatable.html',results=exp)

## testing html table
@app.route('/table')
def table_display():
    return render_template('table.html')

## if condition jinja2 template
@app.route('/successif/<int:score>')
def if_statement_success(score):
    return render_template('if_result.html',results=score)

## Building URL dynamically

@app.route('/newsuccess/<int:score>')
def new_success(score):
    return render_template('result.html',results=score)

@app.route('/newfail/<int:score>')
def newfail(score):
    return render_template('result.html',results=score)

## the function name must match the decorator in order to use url_for.
## because it redirect to the function not the url.
@app.route('/getresult',methods=['GET','POST'])
def get_results():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
        print(f'The average score is {total_score}.')
    else:
        return render_template('getresult.html')
    return redirect(url_for('newfail',score=total_score))

if __name__=="__main__":
    app.run(debug=True)
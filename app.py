from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
'''

# Initialise the app/ flask instance
# WSGI application
# "__name__" entrypoint for the application
app=Flask(__name__)

## homepage is ("/")
## execute the function
## app.route = mapping the URLs to a specific function 
@app.route("/")
def welcome():
    return "Welcome to the webpage!!! This is a Flask course. This should be an amazing course."

@app.route("/index")
def index():
    return "Welcome to the index page."

# entrypoint (first thing the program execute) for the python file.
if __name__=='__main__':
    # host = local_host or can specify port
    # debug=True, able to apply the modification in the script without restarting the host.
    app.run(debug=True)
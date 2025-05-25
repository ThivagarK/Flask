## Put and Delete-HTTP Verbs
## Working with API's--Json
## JSON(javascript object notation) is used for storing and transmitting data.

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in my to do list
## Dictinary exmaple= mongodb or nosql
items=[
    {"id":1,"name":"Item1","description":"This is item 1"},
]
if __name__=='__main__':
    app.run(debug=True)
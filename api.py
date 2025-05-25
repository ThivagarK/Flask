## Put and Delete-HTTP Verbs
## Working with API's--Json
## JSON(javascript object notation) is used for storing and transmitting data.
## jsonify is function in Flask to convert Python data structures into JSON.
## request is object that contains all the data from the Client to Server.
from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in my to do list.
## Dictinary exmaple= mongodb or nosql
items=[
    {"id":1,"name":"Item1","description":"This is item 1."},
    {"id":2,"name":"Item2","description":"This is item 2."}
]

@app.route('/')
def home():
    return "Welcome To The Samaple To Do List App."

## Get: Retrieve all the items.
@app.route('/items')
def get_items():
    return jsonify(items)

## Get: Retriever a specific item using id
@app.route('/items/<int:item_id>')
def get_item(item_id):
## next is built in function that iterate to next item in list white is iter.
## this is comprehension(way to create new sequences such as lsit dictionary)
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

## Post: create a new task
@app.route('/items',methods=['POST'])
def create_item():
    ## if request is not in the json format or name key is not in request.
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description":request.json["description"]
    }
    items.append(new_item)
    ## display purposes
    return jsonify(new_item)

## PUT: Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    ## retrieve item
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    ## update the item using the item name
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

## DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    ## global variable type is used to modify any global variable.
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"results":"Item deleted"})

    


if __name__=='__main__':
    app.run(debug=True)
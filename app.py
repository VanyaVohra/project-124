from flask import Flask, jsonify, request

tasks = [
    {
        'id':1,
        'Contact': u'1234567890',
        'Name': u'Vanya',
        'done': False
    },
    {
        'id':2,
        'Contact': u'0987654321',
        'Name': u'Vivaan',
        'done':False
    }
]

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/products")
def product():
    return "This is a product page!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        }, 400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'Contact': request.json['Contact'],
        'Name': request.json.get('Name', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if __name__ == "__main__":
    app.run(debug=True)
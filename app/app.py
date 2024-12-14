from flask import Flask, request, Response

import json

with open('data.json', 'r') as file:
    data = json.load(file)

app = Flask(__name__)

@app.get("/users")
def users():
    return data["users"]

@app.get("/users/<id>")
def addUser(id):
    return data["users"]

@app.post("/users")
def post_user():
    request.json["id"] = len(data)+1
    data.append(request.json)
    return Response(status=200)

@app.patch("/users/<id>")
def patch_user(id):
    data[int(id)-1][next(iter(request.json))] = request.json[next(iter(request.json))]

    return Response(status=200)

@app.put("/users/<id>")
def put_user(id):
    request.json["id"] = id
    data[id-1] = request.json
    return Response(status=200)

@app.delete("/users/<id>")
def delate_user(id):
    
    return Response(status=200)


if __name__ == "__main__":
    app.run()
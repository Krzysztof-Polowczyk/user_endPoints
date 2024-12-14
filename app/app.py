from flask import Flask, request, Response

import json

with open('data.json', 'r') as file:
    data = json.load(file)

app = Flask(__name__)

@app.get("/users")
def users():
    return data["users"]

@app.get("/users/<id>")
def get_user_via_id(id):
    return next(filter(lambda user: user["id"] == int(id), data["users"]))

@app.post("/users")
def post_user():
    data["leatest_id"] += 1
    request.json["id"] = data["leatest_id"]
    data["users"].append(request.json)
    return Response(status=200)

@app.patch("/users/<id>")
def patch_user(id):
    data["users"][next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(data["users"])))[0]][next(iter(request.json))] = request.json[next(iter(request.json))]

    return Response(status=200)

@app.put("/users/<id>")
def put_user(id):
    request.json["id"] = id
    data["users"][next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(data["users"])))[0]] = request.json
    return Response(status=200)

@app.delete("/users/<id>")
def delate_user(id):
    del data["users"][next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(data["users"])))[0]]
    return Response(status=200)


if __name__ == "__main__":
    app.run()
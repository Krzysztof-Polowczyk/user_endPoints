from flask import Flask, request, Response

import json


app = Flask(__name__)

def get_data():
    if __name__ == "__main__":
        with open('data.json', 'r') as file:
            return json.load(file)
    

@app.get("/users")
def users(inner_data = get_data()):
    return inner_data["users"]

@app.get("/users/<id>")
def get_user_via_id(id, inner_data = get_data()):
    return next(filter(lambda user: user["id"] == int(id), inner_data["users"]))

@app.post("/users")
def post_user( inner_data = get_data()):
    inner_data["leatest_id"] += 1
    request.json["id"] = inner_data["leatest_id"]
    inner_data["users"].append(request.json)
    return Response(status=200)

@app.patch("/users/<id>")
def patch_user(id,  inner_data = get_data()):
    inner_data["users"][next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(inner_data["users"])))[0]][next(iter(request.json))] = request.json[next(iter(request.json))]

    return Response(status=200)

@app.put("/users/<id>")
def put_user(id,  inner_data = get_data()):
    request.json["id"] = id
    inner_data["users"][next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(inner_data["users"])))[0]] = request.json
    return Response(status=200)

@app.delete("/users/<id>")
def delate_user(id,  inner_data = get_data()):
    del inner_data["users"][next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(inner_data["users"])))[0]]
    return Response(status=200)


if __name__ == "__main__":
    app.run()

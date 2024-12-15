from flask import Flask, request, Response

import json


app = Flask(__name__)
if __name__ == "__main__":
    with open('data.json', 'r') as file:
        data = json.load(file)
elif __name__ == "app.app":  
    with open('app\data.JSON', 'r') as file:
        data = json.load(file)
else: 
    data = []
    

@app.get("/users")
def users(inner_data = data):
    print(inner_data, __name__)
    return inner_data["users"], 200

@app.get("/users/<id>")
def get_user_via_id(id, inner_data = data):
    try:
        return  next(filter(lambda user: user["id"] == int(id), inner_data["users"])), 200  
    except StopIteration:
        return StopIteration, 400

@app.post("/users")
def post_user( inner_data = data, inner_request = request):
    try:
        inner_request_json = inner_request.json
    except:
        inner_request_json = inner_request
    inner_data["leatest_id"] += 1
    inner_request_json["id"] = inner_data["leatest_id"]
    inner_data["users"].append(inner_request_json)
    return Response(status=201)

@app.patch("/users/<id>")
def patch_user(id,  inner_data = data, inner_request = request):
    
    try:
        inner_request_json = inner_request.json
    except:
        inner_request_json = inner_request
    try:
        inner_data["users"][next(filter(lambda user: user[1]["id"] == int(id), enumerate(inner_data["users"])))[0]][next(iter(inner_request_json))] = inner_request_json[next(iter(inner_request_json))]
        return Response(status=204)
    except:
        return Response(status=400)
    

@app.put("/users/<id>")
def put_user(id,  inner_data = data, inner_request = request):
    try:
        inner_request_json = inner_request.json
    except:
        inner_request_json = inner_request
    try: 
        inner_request_json["id"] = int(id)
        inner_data["users"][next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(inner_data["users"])))[0]] = inner_request_json  
        return Response(status=204)
    except StopIteration:
        Response(status=400)

@app.delete("/users/<id>")
def delate_user(id,  inner_data = data):
    try:
        print(list(enumerate(inner_data["users"])))
        print(next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(inner_data["users"])))[0])
        del inner_data["users"][next(filter(lambda user: user[1]["id"] == int(id) ,enumerate(inner_data["users"])))[0]]
        return Response(status=204)
    except StopIteration:
        return Response(status=400)




if __name__ == "__main__":
    app.run()

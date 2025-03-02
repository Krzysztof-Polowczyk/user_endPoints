import requests

from app import app
from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_user_get(client):
    assert  200 == client.get("/users").status_code

def test_user_get_via_id(client):
    assert  200 == client.get("/users/1").status_code
    
def test_user_post(client):
    assert  201 == client.post("/users", json={"name": "jan", "lastname": "kowalski"}).status_code

def test_user_patch_via_id(client):
    assert  204 == client.patch("/users/2", json={"name": "jan"}).status_code

def test_user_patch_via_id_with_wrong_id(client):
    assert  400 == client.patch("/users/124", json={"name": "jan"}).status_code

def test_user_put_via_id(client):
    assert client.put("users/1", json={"name": "maciej", "lastname": "mickiewicz"}).status_code == 204

def test_user_delete_via_id(client):
    assert  204 == client.delete("/users/1").status_code

def test_user_delete_via_id_with_wrong_id(client):
    assert  400 == client.delete("/users/124").status_code
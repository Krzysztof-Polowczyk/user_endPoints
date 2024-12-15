from app import post_user
import pytest
import json

@pytest.fixture
def date_testing():
    with open('tests\data_testing.JSON', 'r') as file: return json.load(file)


def test_post_user(date_testing):
    post_user(date_testing, {"name": "krzys", "lastname": "polo"},)
    assert date_testing['users']  == [
        {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},
        {"id": 2, "name": "krzys", "lastname": "polo"},
        {"id": 3, "name": "krzys", "lastname": "polo"},
    ]
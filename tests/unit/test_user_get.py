import pytest
import json
from app import users

@pytest.fixture
def date_testing():
    with open('tests\data_testing.JSON', 'r') as file:
        return json.load(file)



def test_is_users_returning_users(date_testing):
    assert users(date_testing)  == [
        {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},
        {"id": 2, "name": "krzys", "lastname": "polo"}
    ]
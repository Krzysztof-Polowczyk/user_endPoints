import pytest
import json
from app import put_user

@pytest.fixture
def date_testing(): 
    with open('tests\data_testing.JSON', 'r') as file: return json.load(file)

@pytest.mark.parametrize("config",
                            [
        [1, {"name": "hej", "lastname": "hejowski"},[{"id": 1, "name": "hej", "lastname": "hejowski"},{"id": 2, "name": "krzys", "lastname": "polo"}]],
        [6, {"name": "hej", "lastname": "hejowski"},[{"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},{"id": 2, "name": "krzys", "lastname": "polo"}]],
                            ]
                        )
def test_put_user_via_id(date_testing, config):
    put_user(config[0], date_testing, config[1])
    assert date_testing["users"] == config[2]
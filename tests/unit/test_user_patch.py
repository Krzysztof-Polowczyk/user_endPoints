import pytest
import json
from app import patch_user

@pytest.fixture
def date_testing(): 
    with open('tests\data_testing.JSON', 'r') as file: return json.load(file)

@pytest.mark.parametrize("config",
                            [
        [1, {"name": "hej"},[{"id": 1, "name": "hej", "lastname": "Oczkowski"},{"id": 2, "name": "krzys", "lastname": "polo"}]],
        [5, {"name": "hej"},[{"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},{"id": 2, "name": "krzys", "lastname": "polo"}]],
        [2, {"lastname": "zygala"},[{"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},{"id": 2, "name": "krzys", "lastname": "zygala"}]]
                            ]
                        )
def test_patch_user_via_id(date_testing, config):
    patch_user(config[0], date_testing, config[1])
    assert date_testing["users"] == config[2]




    
import pytest
import json
from app import delate_user

@pytest.fixture
def date_testing(): 
    with open('tests\data_testing.JSON', 'r') as file: return json.load(file)

@pytest.mark.parametrize("config",
                            [
        [1, [{"id": 2, "name": "krzys", "lastname": "polo"}]],
        [6, [{"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},{"id": 2, "name": "krzys", "lastname": "polo"}]],
                            ]
                        )
def test_delete_user_via_id(date_testing, config):
    delate_user(config[0], date_testing)
    assert date_testing["users"] == config[1]




    
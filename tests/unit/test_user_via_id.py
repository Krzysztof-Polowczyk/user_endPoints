import pytest
import json
from app import get_user_via_id

@pytest.fixture
def date_testing(): 
    with open('tests\data_testing.JSON', 'r') as file: return json.load(file)

@pytest.mark.parametrize("config",
                            [
        [1, {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}],
        [5, StopIteration]
                            ]
                        )
def test_is_users_returning_users(date_testing, config):
    assert get_user_via_id(config[0], date_testing)[0] == config[1]




    
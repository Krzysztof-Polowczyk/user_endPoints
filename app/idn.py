from app import users
import pytest


def test_ping_endpoint():
    assert users()  == {
    "1": {"name": "Wojciech", "lastname": "Oczkowski"},
    "2": {"name": "krzys", "lastname": "polo"}
    }
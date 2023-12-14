from main import user_auth

import pytest

@pytest.mark.parametrize("a, b", [("standard_user", "123456")])
def test_user_auth(a, b):
    assert user_auth(a, b) == "Epic sadface: Username and password do not match any user in this service"



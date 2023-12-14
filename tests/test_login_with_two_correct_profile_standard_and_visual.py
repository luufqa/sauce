from main import user_auth

import pytest


@pytest.mark.parametrize("a, b", [("standard_user", "secret_sauce"), ("visual_user", "secret_sauce")])
def test_user_auth(a, b):
    assert user_auth(a, b) == "https://www.saucedemo.com/inventory.html"

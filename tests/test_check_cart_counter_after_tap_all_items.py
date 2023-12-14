from main import check_button

import pytest


@pytest.mark.parametrize("a, b", [("standard_user", "secret_sauce"), ("error_user", "secret_sauce")])
def test_user_auth(a, b):
    assert check_button(a, b) == 6

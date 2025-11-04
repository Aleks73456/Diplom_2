import pytest
import helpers

@pytest.fixture
def regist():
    access_token = helpers.regist_user_for_get_access_token()
    headers = {"Authorization": access_token}
    yield headers
    helpers.delete_user(access_token)




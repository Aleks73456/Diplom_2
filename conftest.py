import pytest
import helpers

@pytest.fixture
def regist():
    access_token = helpers.regist_user_for_get_access_token()
    headers = {"Authorization": access_token}
    yield headers
    helpers.delete_user(access_token)


@pytest.fixture
def payload_for_regist():
    helpers.payload_for_regist()
    yield headers
    helpers.delete_user(response.json()['accessToken'])

from http import HTTPStatus
import pytest


from clients.users.public_users_client import PublicUsersClient
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tests.conftest import UserFixture
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code


@pytest.mark.users
@pytest.mark.regression
def test_login(
        function_user: UserFixture,
        public_users_client: PublicUsersClient,
        authentication_client: AuthenticationClient
):

    login_request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
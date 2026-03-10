from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient
from fixtures.users import UserFixture  # Заменяем импорт
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.users
@pytest.mark.regression
class TestAuthentication:
    def test_login(
            self,
            function_user: UserFixture,
            public_users_client: PublicUsersClient,
            authentication_client: AuthenticationClient
    ):

        login_request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        login_response = authentication_client.login_api(login_request)
        login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

        assert_status_code(login_response.status_code, HTTPStatus.OK)
        assert_login_response(login_response_data)
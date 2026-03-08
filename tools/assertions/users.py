from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal
from clients.users.users_schema import UserSchema



def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")



def assert_user(actual: UserSchema, expected: UserSchema) -> None:
    assert_equal(actual.id, expected.id, "User id mismatch")
    assert_equal(actual.email, expected.email, "User email mismatch")
    assert_equal(actual.last_name, expected.last_name, "User last_name mismatch")
    assert_equal(actual.first_name, expected.first_name, "User first_name mismatch")
    assert_equal(actual.middle_name, expected.middle_name, "User middle_name mismatch")


def assert_get_user_response(
    get_user_response: UserSchema,
    create_user_response: UserSchema
) -> None:
    assert_user(
        actual=get_user_response,
        expected=create_user_response.user
    )
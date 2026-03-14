from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
import allure


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Лжидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.type, expected.type, 'type')
    assert_equal(actual.input, expected.input, 'input')
    assert_equal(actual.context, expected.context, 'context')
    assert_equal(actual.message, expected.message, 'message')
    assert_equal(actual.location, expected.location, 'location')


@allure.step("Check validation error response")
def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    """
    Проверяет, что объект ответа API с ошибками валидации (ValidationErrorResponseSchema)
    соответсвует ожидаемому значению.
    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_length(actual.details, expected.details, 'details')

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step("Check internal error response")
def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    Функция для проверки внутренней ошибки.
    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.details, expected.details, 'details')


@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.
    :param actual: Фуктический ответ.
    :raises AssertionError: Если фактический ответ не соответсвует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(details='File not found')
    assert_internal_error_response(actual, expected)
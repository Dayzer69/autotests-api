from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFilesResponseSchema
from tools.assertions.base import assert_equal
from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema
from tools.assertions.errors import assert_validation_error_response
import allure
from config import settings
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("FILES_ASSERTIONS")


@allure.step("Check create file response")
def assert_create_files_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create file response")
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, 'url')
    assert_equal(response.file.filename, request.filename, 'filename')
    assert_equal(response.file.directory, request.directory, 'directory')


@allure.step("Check file")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check file")
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.url, expected.url, 'url')
    assert_equal(actual.filename, expected.filename, 'filename')
    assert_equal(actual.directory, expected.directory, 'directory')


@allure.step("Check get file response")
def assert_get_file_response(get_file_response: GetFilesResponseSchema, create_file_response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание.

    :param get_file_response: Ответ API при запросе данных файла.
    :param create_file_response: Ответ API при создании файла.
    :raises AssertionError: Если данные файла не совпадают.
    """
    logger.info("Check get file response")
    assert_file(get_file_response.file, create_file_response.file)


@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty filename response")
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='string_too_short',
                input='',
                message='Field required',
                location=['body', 'filename']
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty directory response")
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='string_too_short',
                input='',
                message='Field required',
                location=['body', 'directory']
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ получение файла с некорректным айди соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check get file with incorrect file id response")
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='uuid_parsing',
                input='fake.request.id',
                message="Input should be a valid UUID, invalid character: expected an optional prefix of "
                        "`urn:uuid:` followed by [0-9a-fA-F-], found `k` at 3",
                ctx={'error': 'invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `k` at 3'},
                location=['path', 'file_id']
            )
        ]
    )
    assert_validation_error_response(actual, expected)
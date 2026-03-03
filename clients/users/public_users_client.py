from clients.api_client import APIClient, Response
from typing import TypedDict
from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users без авторизации
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создаёт нового пользователя.

        :param request: данные для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/users', json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())


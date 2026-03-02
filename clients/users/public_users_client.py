from clients.api_client import APIClient, Response
from typing import TypedDict


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
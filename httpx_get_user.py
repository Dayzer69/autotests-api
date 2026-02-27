import httpx
from tools import fakers


# Создаём пользователя
create_user_payload = {
  "email": fakers.get_random_email(),
  "password": "password",
  "lastName": "Doe",
  "firstName": "Jonh",
  "middleName": "mid"
}

user_response = httpx.post('http://localhost:8000/api/v1/users', json=create_user_payload)
print(user_response.status_code)
print(user_response.json())


# Проходим аутентификацию
login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload['password']
}

login_responxe = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
print(login_responxe.status_code)
print(login_responxe.json())

# Получаем данные пользователя
user_access_token = {
  'Authorization': f'Bearer {login_responxe.json()["token"]["accessToken"]}'
}

user_info_response = httpx.get(
  f'http://localhost:8000/api/v1/users/{user_response.json()["user"]["id"]}',
  headers=user_access_token
)
print(user_info_response.status_code)
print(user_info_response.json())
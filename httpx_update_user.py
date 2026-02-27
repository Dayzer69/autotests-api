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

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
print(login_response.status_code)
print(login_response.json())


# Изменяем данные пользователя
update_user_header = {
    'Authorization': f'Bearer {login_response.json()['token']['accessToken']}'
}

update_user_payload = {
  "email": fakers.get_random_email(),
  "lastName": "NewLastName",
  "firstName": "NewFirstName",
  "middleName": "NewMiddleName"
}

update_user_response = httpx.patch(
    f'http://localhost:8000/api/v1/users/{user_response.json()["user"]["id"]}',
    headers=update_user_header,
    json=update_user_payload
)
print(update_user_response.status_code)
print(update_user_response.json())
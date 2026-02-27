import httpx
from tools import fakers


payload = {
  "email": fakers.get_random_email(),
  "password": "password",
  "lastName": "Doe",
  "firstName": "Jonh",
  "middleName": "mid"
}

user_response = httpx.post('http://localhost:8000/api/v1/users', json=payload)
print(user_response.status_code)
print(user_response.json())

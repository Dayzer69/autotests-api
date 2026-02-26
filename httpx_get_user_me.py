import httpx

login_data = {
    "email": "tishinanton@test.com",
    "password": "123456"
}


login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_data)
print(login_response.status_code)
print(login_response.json())


me_header = {
    'Authorization': f'Bearer {login_response.json()["token"]["accessToken"]}'
}

me_response = httpx.get('http://localhost:8000/api/v1/users/me',
                        headers=me_header)

print(me_response.json())
print(me_response.status_code)
import requests
import os

url =  'https://www.instagram.com'

requests.post(url, allow_redirects=True, data={
    'emailOrPhone': 'plechac.jakub.test@seznam.cz',
    'fullName': 'Jakub Plechac',
    'username': 'test_request_user69',
    'password': 'my_password123',
})

print(f'sended {username} and {password}')

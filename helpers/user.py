import random
import string

import requests

from config import URL_SERVICE


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_unique_user_data():
    return {
        'email': f'{generate_random_string(8)}@{generate_random_string(5)}.ru',
        'password': generate_random_string(10),
        'name': generate_random_string(8),
    }


def register_user():
    payload = generate_unique_user_data()
    response = requests.post(f'{URL_SERVICE}/auth/register', json=payload)
    return response, payload


def delete_user(access_token):
    return requests.delete(
        f'{URL_SERVICE}/auth/user',
        headers={'Authorization': access_token},
    )

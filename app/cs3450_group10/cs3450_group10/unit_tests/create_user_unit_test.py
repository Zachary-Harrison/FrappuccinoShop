import requests
import os
import binascii




def generate_csrf_token():
    """Return a randomly generated string for use as CSRF Tokens

    Returns:
        `str`
    """
    return binascii.hexlify(os.urandom(32)).decode() 


url = 'http://127.0.0.1:3000/shop_app/register'
payload = {
    'csrfmiddlewaretoken': generate_csrf_token(),
    'username': 'Unit Test User',
    'password1': 'thisIsaNewPasswordTest!1',
    'password2': 'thisIsaNewPasswordTest!1',
    'Create+User': 'SUbmit+Query'
}

x = requests.post(url, payload)
print(x)
#print(generate_csrf_token())
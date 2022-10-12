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
#payload = {
#    'csrfmiddlewaretoken': generate_csrf_token(),
#    'username': 'UnitTestUser',
#    'password1': 'thisIsaNewPasswordTest!1',
#    'password2': 'thisIsaNewPasswordTest!1',
#    'Create+User': 'Submit+Query'
#}


client = requests.session()

client.get(url)
session = requests.Session()
response = session.get(url)
cookiesDict = session.cookies.get_dict()
print(cookiesDict)

csrftoken = cookiesDict['csrftoken']
print(csrftoken)

# Pass CSRF token both in login parameters (csrfmiddlewaretoken)
# and in the session cookies (csrf in client.cookies)
login_data = dict( csrfmiddlewaretoken=csrftoken, username='userUnitTest', password1='UserTestUnit456',password2='UserTestUnit456', next='/')
r = client.post(url, data=login_data, headers=dict(Referer=url))

#print(requests.get(url))

x = requests.post(url, login_data)
print(r)
#print(generate_csrf_token())
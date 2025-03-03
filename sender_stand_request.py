import data
import configuration
import requests

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)
def get_new_user_token():
    token = response.json()["authToken"]
    return token
def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.headers)
import requests

pixela_api = "https://pixe.la/v1/users"
user_params = {
    "token" : "12345678iu",
    "username" : "raihank",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

response = requests.post(url=pixela_api, json=user_params)
print(response.text)


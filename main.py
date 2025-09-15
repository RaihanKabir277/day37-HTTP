import requests


USERNAME = "raihank"
TOKEN = "12345678iu"
pixela_api = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
#  ------ step 1  response api endpoint ------
# response = requests.post(url=pixela_api, json=user_params)
# print(response.text)

# ------------ step 2 graph api endpoint -----
graph_endpoint = f"{pixela_api}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN" : TOKEN,
}

graph_config = {
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai",
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)



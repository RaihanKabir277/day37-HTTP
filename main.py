import requests
from datetime import datetime

USERNAME = "raihank"
TOKEN = "12345678iu"
GRAPH_ID = "graph1"
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
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai",
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)


#  -------- step 4 post value to the graph --------
value_endpoint = f"{pixela_api}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))
DATE = today.strftime("%Y%m%d")

value_config = {
    "date" : DATE,
    "quantity" : "9",
}

# value_response = requests.post(url=value_endpoint, json=value_config, headers=headers)
# print(value_response.text)

# ----------- put method ----------
put_endpoint = f"{pixela_api}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

update_data = {
    "quantity" : "12.5",

}

update_response = requests.put(url=put_endpoint, json=update_data, headers=headers)
print(update_response.text)

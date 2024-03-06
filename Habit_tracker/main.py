import requests
from datetime import datetime

USERNAME = "ikay"
TOKEN = "45trfg9o7ui875rfg"
pixela_ENDPOINT = "https://pixe.la/v1/users "
GRAPH_ID = "graph34"


################# Creating a new username(request.post) #########
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_ENDPOINT, json=user_parameters)
# print(response.text)


############ Creating a graph ################
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{pixela_ENDPOINT}/{USERNAME}/graphs"

# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


########## post a pixel  (request.post) ############
create_pixel_endpoint = f"{pixela_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=11, day=18)
date = today.strftime("%Y%m%d")

pixel_body = {
    "date": date,
    "quantity": str(input("How many kilometers did you cycle today")),
}

# response = requests.post(create_pixel_endpoint, json=pixel_body, headers=headers)
# print(response.text)

################ Update a pixel (request.put)###########
update_params = {
    "quantity": "7.8",
}

update_pixel_endpoint = f"{pixela_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

# response = requests.put(update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

############ Delete a pixel (request.delete)########

delete_pixel_endpoint = f"{pixela_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

# response = requests.delete(delete_pixel_endpoint, headers=headers)
# print(response.text)

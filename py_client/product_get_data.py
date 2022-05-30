import requests


def get_product_data(endpoint):
    try:
        get_response = requests.get(endpoint)
        # print(get_response.json())
        json_response = get_response.json()
        return json_response
    except Exception as e:
        return {'error':e}
# get_product_data('http://127.0.0.1:8000/api/v1/products/6')


# endpoint = "http://localhost:8000/api/products/1/update/"

# data = {
#     'title': 'Hello World my old friend',
#     'price': 22323.22
# }

# get_response = requests.put(endpoint, json=data)

# print(get_response.json())

import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_name(params={}):
    response = generate_request('https://www.banxico.org.mx/SieAPIRest/service/v1/series/', params)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return ''
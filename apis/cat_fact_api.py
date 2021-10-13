import requests

url = 'https://catfact.ninja/fact'

def get_random_fact():

    try:
        response = requests.get(url).json()
        return response['fact']
    except Exception as e:
        print('Can\'t fetch fact because', e)  # TODO replace with better error handling

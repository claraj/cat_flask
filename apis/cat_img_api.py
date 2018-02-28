import requests
import xml.etree.ElementTree as ET


url = 'http://thecatapi.com/api/images/get'
def get_cat(category):

    try:
        params = {
        'results_per_page': 1,
        'category': category,
        'format': 'xml'
        }

        response = requests.get(url, params)
        xml = ET.fromstring(response.text)
        img_url = xml.findall('.//url')[0].text  # First element with this tag

        return img_url

    except Exception as e:
        print('Error fetching data because ', e) # Replace this

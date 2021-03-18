import requests
import os 

search_url = 'https://api.thecatapi.com/v1/images/search'
categories_url = 'https://api.thecatapi.com/v1/categories'

CAT_API_KEY = os.environ.get('CAT_API_KEY')

def get_cat_img(category):

    try:
        headers = {
            'x-api-key': CAT_API_KEY
        }

        # get category list 
        categories_response = requests.get(categories_url, headers=headers).json()

        # convert category into category id 
        category_info = next( category_ob for category_ob in categories_response if category_ob['name'] == category)
        category_id = category_info['id']
        
        params = {
            'limit': 1,
            'category_ids': category_id
        }

        response = requests.get(search_url, params=params, headers=headers).json()
        data = response[0]  # first image
        img_url = data['url']
        return img_url

    except Exception as e:
        print('Error fetching data because', e)  # TODO Replace this with better error handling


if __name__ == '__main__':
    get_cat('space')   # example API call
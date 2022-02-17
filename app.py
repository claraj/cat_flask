from flask import Flask, request, render_template, redirect

from apis import cat_img_api, cat_fact_api, cat_video_api
from database import db 

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/get-cat')
def get_cat():
    # request.args is a dictionary-like object built from the data in the form in index.html
    category = request.args.get('category') or 'space'  # set a default
    
    cat_img_url = cat_img_api.get_cat_img(category)
    cat_fact = cat_fact_api.get_random_fact()
    cat_video = cat_video_api.cat_video(category)

    return render_template('cat.html', category=category, cat_img_url=cat_img_url, cat_fact=cat_fact, cat_video=cat_video)
    

@app.route('/store-data')
def store_data():
    # this doesn't do anything except to be an example for how a real db call would be made
    # to code in the database/db.py file
    result = db.store_data('example')
    print(result)
    return redirect('/')


@app.route('/favorites')
def favorites_page():
    # TODO get favorites from the database, include in response
    return render_template('favorites.html')


if __name__ == '__main__':
    app.run()

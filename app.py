from flask import Flask, request, render_template

from apis import cat_img_api, cat_fact_api, cat_video_api

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/get-cat')
def get_cat():
    category = request.args.get('category') #or 'space'  # set a default

    cat_img_url = cat_img_api.get_cat(category)
    cat_fact = cat_fact_api.get_random_fact()
    cat_video = cat_video_api.cat_video(category)

    if cat_img_url and cat_fact and cat_video:
        return render_template('cat.html', cat_img=cat_img_url, category=category, cat_fact=cat_fact, cat_video=cat_video)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run()

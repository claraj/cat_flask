from flask import Flask, request, render_template

from apis import cat_img_api, cat_fact_api

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/get-cat')
def get_cat():
    category = request.args.get('category') #or 'space'  # set a default
    cat_img_url = cat_img_api.get_cat(category)

    cat_fact = cat_fact_api.get_random_fact()

    if cat_img_url:
        return render_template('cat.html', cat_img=cat_img_url, category=category, cat_fact=cat_fact)

    return render_template('error.html')


if __name__ == '__main__':
    app.run()

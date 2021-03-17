# Cat Site

Uses [The Cat API](http://thecatapi.com/) and [Cat Facts](https://catfact.ninja/#!/Cat_Facts/fact) API and the [YouTube](https://developers.google.com/youtube/v3/quickstart/python) API.

500 image from [HTTP Cats](https://http.cat/).

## To install and run

* Create a [YouTube API key](https://developers.google.com/youtube/registering_an_application). You only need an API key, not OAuth credentials.  
* Create an environment variable **YOUTUBE_API_KEY** holding your key.
* Create and activate virtual environment using Python 3
* `pip install -r requirements.txt`
* `python app.py`

App will be running on http://127.0.0.1:5000

## To Do

Better error handling. A new module that manages all of the API requests. All kinds of other things.

# Tests 

Placeholder tests provided. To run tests, use this command from the root directory of the project

`python -m unittest discover tests`

The discover option will find and run all the tests in the tests directory. 
import requests


def clean_post_data(post_data):
    """
    Removes None values from data, so that it can posted to Django's test
    client without TypeError being raised in Django 2.2+
    """
    return {
        key: value for key, value in post_data.items()
        if value is not None
    }


def create_response(status_code, json_body={}, content=None):
    response = requests.Response()
    response.status_code = status_code
    response.json = lambda: json_body
    response._content = content
    return response

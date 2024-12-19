from flask import Blueprint, render_template, session, redirect, url_for
import requests

main_page_blueprint = Blueprint('main_page', __name__)

@main_page_blueprint.route('/')
def main_page():
    if 'user_id' in session:
        user_information = requests.get(f'http://127.0.0.1:1234/api/v1/users/{session["user_id"]}').json()
        return render_template('index.html', user_information=user_information)
    
    return render_template('index.html')
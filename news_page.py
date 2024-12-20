from flask import Blueprint, render_template, session, redirect, url_for, request
from markupsafe import Markup
from datetime import datetime
import locale

import requests

news_page_blueprint = Blueprint('news_page', __name__)

@news_page_blueprint.route('/news/<int:news_id>', methods=['GET', 'POST'])
def news_page(news_id):
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'ru_RU')
        except:
            pass
    if request.method == 'GET':
        session['page'] = f'/news/{news_id}'

        news = requests.get(f'http://127.0.0.1:1234/api/v1/news/{news_id}').json()
        text = Markup(news['text'])
        author_information = requests.get(f'http://127.0.0.1:1234/api/v1/users/{news["author_id"]}').json()

        date_object = datetime.strptime(news['date'].split()[0], "%Y-%m-%d")
        formatted_date = date_object.strftime("%B, %d")

        if 'user_id' in session:
            user_information = requests.get(f'http://127.0.0.1:1234/api/v1/users/{session["user_id"]}').json()
            return render_template('news copy.html', 
                                   news=news, 
                                   text=text, 
                                   author=author_information,
                                   formatted_date=formatted_date,
                                   user_information=user_information
                                   )

        return render_template('news copy.html', 
                               news=news, 
                               text=text, 
                               author=author_information,
                               formatted_date=formatted_date
                               )
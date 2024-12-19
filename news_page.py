from flask import Blueprint, render_template, session, redirect, url_for, request

news_page_blueprint = Blueprint('news_page', __name__)

@news_page_blueprint.route('/news/<int:news_id>', methods=['GET', 'POST'])
def news_page(news_id):
    if request.method == 'GET':
        return render_template('news.html')
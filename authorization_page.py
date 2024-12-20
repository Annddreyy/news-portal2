from flask import Blueprint, render_template, session, redirect, url_for, request
import requests
import hashlib

authorization_page_blueprint = Blueprint('authorization_page', __name__)

@authorization_page_blueprint.route('/authorization', methods=['GET', 'POST'])
def authorization_page():
    if request.method == 'GET':
        return render_template('authorization.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    users = requests.get('http://127.0.0.1:1234/api/v1/users').json()
    
    password = password.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(password)
    hash_code = sha256.hexdigest()

    for user in users:
        if user['login'] == login and user['password'] == hash_code:
            session['user_id'] = user['id']
            return redirect(session['page'])

    return render_template('authorization.html', error_message='Неверный логин или пароль!')

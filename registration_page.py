from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
import requests
import hashlib
import base64
from github import Github
import string
import random

registration_page_blueprint = Blueprint('registration_page', __name__)

@registration_page_blueprint.route('/registration', methods=['GET', 'POST'])
def registration_page():
    if request.method == 'GET':
        return render_template('registration.html')
    
    surname = request.form.get('surname')
    name = request.form.get('name')
    patronymic = request.form.get('patronymic')

    login = request.form.get('login')
    password = request.form.get('password')

    password = password.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(password)
    hash_code = sha256.hexdigest()

    photo = request.files['photo']
    photo = photo.read()
    image_data = bytearray(photo)

    image = create_image(image_data, 'users/', '.png')

    user = {
        'surname': surname,
        'name': name,
        'patronymic': patronymic,
        'login': login,
        'password': hash_code,
        'photo': image
    }

    message = requests.post(url='http://127.0.0.1:1234/api/v1/users', json=user)
    message.raise_for_status() 
    message = message.json()

    if message.get('status') == 'ok':
        session['user_id'] = message.get('id')
        
        return redirect(session['page'])
    
    return render_template('registration.html', error_message='Произошла ошибка, попробуйте снова!')

def create_image(image_path, folder, file_type):
    image_bytes = bytes(image_path)

    github_token = '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'

    g = Github(github_token)

    repo = g.get_user().get_repo('news-portal-images')
    file_name = generate_random_filename(16) + file_type
    repo.create_file(folder + file_name, 'Add file', image_bytes)

    return file_name

def generate_random_filename(length=16):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))


from flask import Flask
from datetime import timedelta
from main_page import main_page_blueprint
from authorization_page import authorization_page_blueprint
from registration_page import registration_page_blueprint
from news_page import news_page_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = '12foefwjf039423wd2808r'

app.permanent_session_lifetime = timedelta(minutes=1)

app.register_blueprint(main_page_blueprint)
app.register_blueprint(authorization_page_blueprint)
app.register_blueprint(registration_page_blueprint)
app.register_blueprint(news_page_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
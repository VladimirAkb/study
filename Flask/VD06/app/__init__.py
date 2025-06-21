from flask import Flask

#создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)
app.config['SECRET_KEY'] = '_pass_word_'

from app import routes
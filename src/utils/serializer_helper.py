from itsdangerous import URLSafeTimedSerializer
from flask import Flask
from src import configs

app = Flask(__name__)

app.config.from_object(configs.get('default'))

key = app.config['SECRET_KEY']
salt = app.config['SECURITY_LOGIN_SALT']
time = app.config['MAX_AGE']


def get_serializer():
    return URLSafeTimedSerializer(key, salt)


def serialize_data(data):
    return get_serializer().dumps(data)


def deserialize_data(data):
    return get_serializer().loads(data, time*30)

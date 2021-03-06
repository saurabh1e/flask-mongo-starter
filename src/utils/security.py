from flask import abort
from flask_security import Security, MongoEngineUserDatastore
from src.user import models
from .serializer_helper import deserialize_data

user_data_store = MongoEngineUserDatastore(models.dc, models.User, models.Role)


def callback(header):

    try:
        user_data = deserialize_data(header)
        user_id = user_data[0]
        return user_data_store.get_user(user_id)
    except (ValueError, TypeError):
        return abort(403)


def token_loader(data):

    try:
        user_data = deserialize_data(data)
        user_id = user_data[0]
        return user_data_store.get_user(user_id)
    except (ValueError, TypeError):
        return abort(403)


class FlaskSecurityAdmin(Security):

    def __init__(self,  **kwargs):
        super(FlaskSecurityAdmin, self).__init__(datastore=user_data_store, **kwargs)

    def init_app(self, app, datastore=None, register_blueprint=True,
                 login_form=None, confirm_register_form=None,
                 register_form=None, forgot_password_form=None,
                 reset_password_form=None, change_password_form=None,
                 send_confirmation_form=None, passwordless_login_form=None,
                 anonymous_user=None):
        state = super(FlaskSecurityAdmin, self).init_app(app, datastore=user_data_store)
        state.login_manager.header_callback = callback
        state.login_manager.token_callback = token_loader
        pass

security = FlaskSecurityAdmin()

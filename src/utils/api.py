from src.flask_mongorest import MongoRest
from src.flask_mongorest.views import ResourceView
from src.flask_mongorest.resources import Resource
from .blue_print import bp


class DelayedApp(object):

    def __init__(self):
        self.url_rules = []

    def add_url_rule(self, *args, **kwargs):
        self.url_rules.append((args, kwargs))

    def register_blueprint(self, bp):
        return True


class FlaskMongoRestFactory(MongoRest):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
        else:
            self.app = DelayedApp()
        super(FlaskMongoRestFactory, self).__init__(self.app, **{'url_prefix': bp.url_prefix})

    def init_app(self, app):
        if hasattr(self, 'app'):
            if isinstance(self.app, DelayedApp):
                for args, kwargs in self.app.url_rules:
                    app.add_url_rule(*args, **kwargs)
        self.app = app

api = FlaskMongoRestFactory()


class BaseResource(Resource):

    default_limit = 20
    max_limit = 50


class BaseResourceView(ResourceView):
    # authentication_methods = [roles_accepted('admin'), auth_token_required]
    pass

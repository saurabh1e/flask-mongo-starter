from src.flask_admin.contrib.mongoengine import ModelView

from src import admin
from src.user.models import User, Role


class BaseView(ModelView):
    pass

admin.add_view(BaseView(User))
admin.add_view(BaseView(Role))

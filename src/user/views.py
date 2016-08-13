from src.flask_mongorest.methods import Create, Fetch, List, BulkUpdate, Delete, Update

from src import api, BaseResourceView
from .resources import UserResource


@api.register()
class UserResourceView(BaseResourceView):

    resource = UserResource

    methods = [Create, Update, Fetch, List, Delete, BulkUpdate]

from flask_security import UserMixin, RoleMixin
from src import dc, BaseDocument


class UserProfile(dc.EmbeddedDocument, BaseDocument):

    first_name = dc.StringField(max_length=127)
    last_name = dc.StringField(max_length=127)
    date_of_birth = dc.DateTimeField()


class Address(dc.EmbeddedDocument, BaseDocument):

    address_line1 = dc.StringField(max_length=127)
    address_line2 = dc.StringField(max_length=127)

    locality = dc.ReferenceField('Locality')


class User(dc.Document, UserMixin, BaseDocument):

    email = dc.EmailField(max_length=127)
    password = dc.StringField(max_length=255)
    number = dc.IntField()

    active = dc.BooleanField(default=False)
    confirmed_at = dc.DateTimeField()
    last_login_at = dc.DateTimeField()
    current_login_at = dc.DateTimeField()
    last_login_ip = dc.StringField(max_length=55)
    current_login_ip = dc.StringField(max_length=55)
    login_count = dc.IntField()
    is_owner = dc.BooleanField(default=False)

    roles = dc.ListField(dc.ReferenceField('Role'))

    user_profile = dc.EmbeddedDocumentField('UserProfile')


class Role(dc.Document, RoleMixin, BaseDocument):
    name = dc.StringField(max_length=55)


class Locality(dc.Document, BaseDocument):

    name = dc.StringField(max_length=127)
    city = dc.ReferenceField('City')


class City(dc.Document, BaseDocument):

    name = dc.StringField(max_length=127)

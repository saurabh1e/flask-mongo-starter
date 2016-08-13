from cleancat import Schema, MongoEmbeddedReference, List
from .models import User, Role, UserProfile


class RoleSchema(Schema):
    class Meta:
        model = Role


class UserProfileSchema(Schema):
    class Meta:
        model = UserProfile


class UserSchema(Schema):

    class Meta:
        model = User

        roles = List(MongoEmbeddedReference(Role, RoleSchema))
        user_profile = MongoEmbeddedReference(UserProfile, UserProfileSchema)



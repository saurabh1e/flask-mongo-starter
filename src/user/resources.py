from src import BaseResource
from .schemas import User, UserSchema, UserProfile, UserProfileSchema, Role, RoleSchema


class RoleResource(BaseResource):

    document = Role
    schema = RoleSchema


class UserProfileResource(BaseResource):

    document = UserProfile
    schema = UserProfileSchema


class UserResource(BaseResource):
    document = User
    schema = UserSchema

    related_resources = {
        'roles': RoleResource,
        'user_profile': UserProfileResource
    }




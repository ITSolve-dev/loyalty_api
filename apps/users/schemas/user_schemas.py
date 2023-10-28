from core import OrmSchema, DateTimeMixinSchema

from ..entities import UserEntity


class UserSchema(UserEntity, OrmSchema):
    pass


class CreateUserSchema(UserEntity):
    pass


class RetrieveUserSchema(UserSchema, DateTimeMixinSchema):
    pass


# TODO: Make all optional
class UpdateUserSchema(UserEntity):
    pass


class DeleteUserSchema(OrmSchema):
    pass

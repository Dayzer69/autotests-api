from pydantic import BaseModel, EmailStr, Field


class ShortUserSchema(BaseModel):
    email: EmailStr = 'user@example.com'
    last_name: str = Field(alias='lastName', default='string')
    first_name: str = Field(alias='firstName', default='string')
    middle_name: str = Field(alias='middleName', default='string')


class UserSchema(ShortUserSchema):
    id: str = 'string'


class CreateUserRequestSchema(ShortUserSchema):
    password: str = 'string'


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


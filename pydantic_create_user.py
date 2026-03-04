from pydantic import BaseModel, EmailStr, Field


class ShortUserSchema(BaseModel):
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class UserSchema(ShortUserSchema):
    id: str


class CreateUserRequestSchema(ShortUserSchema):
    password: str


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


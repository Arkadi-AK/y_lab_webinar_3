import re
import uuid as uuid_pkg
from datetime import datetime

from pydantic import BaseModel, Field, validator

__all__ = (
    "Token",
    "UserLogin",
    "UserModel",
    "UserCreate",
    "UserUpdate"
)


class UserBase(BaseModel):
    username: str = Field(min_length=4, max_length=20)


class UserModel(UserBase):
    uuid: uuid_pkg.UUID
    email: str
    created_at: datetime
    is_superuser: bool
    is_active: bool


class Token(BaseModel):
    access_token: str
    refresh_token: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    password: str = Field(min_length=4, max_length=30)
    email: str = Field(min_length=6, max_length=25)

    @validator("email")
    def check_email(cls, val):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

        if not re.match(pattern, val):
            raise ValueError('Неправильный адрес email')
        return val


class UserUpdate(BaseModel):
    username: str = Field(default=None, min_length=4, max_length=20)
    email: str = Field(default=None, min_length=6, max_length=25)

    @validator("email")
    def check_email(cls, val):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

        if val is None:
            return val

        if not re.match(pattern, val):
            raise ValueError('Неправильный адрес email')
        return val

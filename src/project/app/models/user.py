from typing import Optional

from .base import ApiBaseModel


class UserResponse(ApiBaseModel):
    """ Модель `Пользователь` """
    user_id: int
    user_email: str
    fullname: str
    join_date: str
    is_active: bool = False
    data_1c: Optional[str]
    uuid_1c: Optional[str] = ""

    class Config:
        orm_mode: True

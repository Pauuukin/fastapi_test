from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from ...models.user import UserResponse

router = APIRouter()


@router.get("/users/{id}/", response_model=UserResponse)
async def get_user_id(id: int) -> UserResponse:
    """ Вернуть пользователя """
    # заглушка с данными
    user = {
        "user_id": id,
        "user_email": "user_email",
        "fullname": "fullname",
        "join_date": "2022.05.05",
        "is_active": False,
        "data_1c": "{}",
        "uuid_1c": "some-uuid-132-4142",
    }

    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User is not found")

    return UserResponse(
        user_id=user['user_id'],
        user_email=user['user_email'],
        fullname=user['fullname'],
        join_date=user['join_date'],
        is_active=user['is_active'],
        data_1c=user['data_1c'],
        uuid_1c=user['uuid_1c'],
    )

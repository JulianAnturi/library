from fastapi import APIRouter, Request, Response
from app.http.controllers.users_controller import UserController
from app.http.schemas.user_schema import UserSchema



users_router = APIRouter(
    tags=["users"]
)

bc = UserController()

## Users Routes Resource
@users_router.get('/users')
def users_all(request: Request):
    return bc.show_all()

@users_router.post('/users')
def users_save(user: UserSchema):
    return bc.save_record(user)

# @users_router.put('/users/{record_id}')
# def users_update(user: UserSchema):
#     return  bc.update_record(record_id,user)

@users_router.get('/users/{record_id}')
def users_one(record_id: int):
    return bc.show_one(record_id)

@users_router.delete('/users/{record_id}')
def users_delete(record_id: int):
    return bc.destroy(record_id)


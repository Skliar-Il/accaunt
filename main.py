from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.database import User, db
from auth.shemas import UserCreate, UserRead, UserUpdate
from auth.auth import auth_backend, current_active_user, fastapi_users
from fastapi_users.db import SQLAlchemyUserDatabase
from auth.user_manager import get_user_maneger 


app=FastAPI(
    title="test"
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
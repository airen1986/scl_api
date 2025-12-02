from fastapi import APIRouter, Depends
from ..core.config import settings
from ..core.users import register_user
from ..db.connection import master_connection
from app.services.users_service import get_user, list_users

router = APIRouter()

@router.get("/{user_id}")
def read_user(user_id: int):
    return "Hello"

@router.get("/")
def read_users():
    master_db_url = settings.MASTER_DB
    this_dict = {"MASTER_DB": master_db_url}
    return this_dict


@router.post("/sign-up")
def signup_user(user_data: dict):
    # TODO: Implement user signup logic
    user_name = user_data.get("user_name")
    display_name = user_data.get("display_name")
    password = user_data.get("password")

    with master_connection() as conn:
        result = register_user(conn, user_name, password, display_name)

    return {"message": result}
from fastapi import APIRouter, Depends
from ...core.config import settings
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

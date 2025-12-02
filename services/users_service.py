from app.repositories.users_repo import get_user_repo, list_users_repo

def get_user(conn, user_id):
    return get_user_repo(conn, user_id)

def list_users(conn):
    return list_users_repo(conn)

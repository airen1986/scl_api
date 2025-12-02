def get_user_repo(conn, user_id: int):
    sql = "SELECT id, name, email FROM users WHERE id = ?"
    return conn.execute(sql, [user_id]).fetchone()

def list_users_repo(conn):
    sql = "SELECT id, name, email FROM users"
    return conn.execute(sql).fetchall()

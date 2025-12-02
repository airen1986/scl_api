import re
import hashlib

def register_user(conn, username, password, display_name=None):
    """
    Registers a new user with the given username and password.
    """
    # Validate if username is a valid email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, username):
        raise "Username must be a valid email address"
    # Implementation goes here
    query = "select IsActive from S_Users where Email = ?"
    row = conn.execute(query, (username,)).fetchone()
    if row:
        is_active = row[0]
        if is_active == 1:
            return "User already exists and is active"
        return "User already exists but is inactive"
    # Hash the password (placeholder - implement actual hashing)
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    password_salt = "static_salt"  # Placeholder - implement actual salt generation

    role_id = 0 # Default role ID for new users

    insert_query = """
                    INSERT INTO S_Users (Email, PasswordHash, DisplayName, PasswordSalt, IsActive, RoleId)
                    VALUES (?, ?, ?, ?, 1, ?)
                    """
    conn.execute(insert_query, (username, password_hash, display_name, password_salt, role_id))
    return "User registered successfully"


def send_activation_email(user_email, activation_code, url):
    """
    Sends an account activation email to the user.
    """
    activation_link = f"{url}/activate?code={activation_code}"
    email_subject = "Activate Your Account"
    email_body = f"Please click the following link to activate your account: {activation_link}"
    
    # Placeholder for sending email logic
    print(f"Sending email to: {user_email}")
    print(f"Subject: {email_subject}")
    print(f"Body: {email_body}")
    
    return "Activation email sent"
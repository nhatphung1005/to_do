def register(username, password):
    user = get_user_by_email(username)
    if user:
        raise ValueError("User already exists")
    
    user = create_user(username, password)
    return user
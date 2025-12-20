def normalize_username(username):
    username = username.strip()
    username = username.lower()
    
    if len(username) < 3:
        return None
    if " " in username:
        return None
    
    return username

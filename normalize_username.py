cache = {}

def normalize_username(username: str) -> str | None:
    if username in cache:
        return cache[username]
    
    username = username.strip().lower()
    if len(username) < 3 or " " in username:
        return None
    
    cache[username] = username
    return username


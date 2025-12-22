def normalize_username(username: str) -> str | None:
    username = username.strip().lower()
    if len(username) < 3 or " " in username:
        return None
    return username

def is_valid_username(username: str) -> bool:
    return normalize_username(username) is not None

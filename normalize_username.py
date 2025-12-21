def normalize_username(username: str) -> str | None:
    username = username.strip().lower()
    if len(username) < 3 or " " in username:
        return None
    return username


cache = {}

def get_normalized_username(raw_username: str) -> str | None:
    if raw_username in cache:
        return cache[raw_username]
    result = normalize_username(raw_username)
    cache[raw_username] = result
    return result



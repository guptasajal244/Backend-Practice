def remove_duplicates(names):
    seen = {}
    unique_names = []
    for name in names:
        if name not in seen:
            seen[name] = True
            unique_names.append(name)
            
    return unique_names


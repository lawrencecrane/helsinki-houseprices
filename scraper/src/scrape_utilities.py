def safe_get(x, attr):
    if (x == None):
        return None

    return x.get(attr)

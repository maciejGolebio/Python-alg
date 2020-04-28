def generate_hashtag(s: str):
    if len(s) == 0:
        return False
    hashtag: str = '#' + s.title().replace(' ', '')
    if len(hashtag) > 140:
        return False
    return hashtag

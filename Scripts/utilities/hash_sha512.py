import hashlib


def double_hash_sha512(text: str):
    return hash_sha512(hash_sha512(text))


def hash_sha512(text: str):
    return hashlib.sha512(text.encode()).hexdigest()

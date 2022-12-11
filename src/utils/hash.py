from hashlib import sha256

def hash_str(value: str):
    """
    Converts the given str to Hash
    """
    return sha256(value.encode()).hexdigest()
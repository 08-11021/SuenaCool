import hashlib

def toMd5(password):
    md = hashlib.md5()
    md.update(password)
    encoded = md.hexdigest()
    return encoded

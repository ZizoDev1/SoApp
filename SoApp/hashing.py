import hashlib


def HashingInfo(input_string):
    if input_string is None:
        raise ValueError("Input string cannot be None")

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the input string
    md5_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    return md5_hash.hexdigest()
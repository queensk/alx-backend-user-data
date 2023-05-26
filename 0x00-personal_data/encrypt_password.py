#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string
    """
    password_bytes = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    returns a boolean indicating if the password matches the hashed password
    """
    password_bytes = password.encode()
    return bcrypt.checkpw(password_bytes, hashed_password)

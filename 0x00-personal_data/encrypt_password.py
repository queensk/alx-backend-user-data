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

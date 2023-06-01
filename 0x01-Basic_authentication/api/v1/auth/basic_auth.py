#!/usr/bin/env python3
"""
class BasicAuth module
"""
from .auth import Auth
from re import fullmatch
import base64
import binascii
from typing import Tuple, TypeVar
from models.user import User



class BasicAuth(Auth):
    """
    Create a class BasicAuth that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header
        """
        if isinstance(authorization_header, str):
            pattern = r'Basic (?P<token>.+)'
            field_match = fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group("token")
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        decoded value of a Base64 string
        """
        if base64_authorization_header is not None and isinstance(
                base64_authorization_header, str):
            try:
                decode_str = base64.b64decode(
                    base64_authorization_header, validate=True)
                return decode_str.decode("utf-8")
            except (binascii.Error, UnicodeDecodeError):
                return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        returns the user email and password from the Base64 decoded value.
        """
        if isinstance(decoded_base64_authorization_header, str):
            pattern = r'(?P<user>[^:]+):(?P<password>.+)'
            match = fullmatch(
                pattern, decoded_base64_authorization_header.strip())
            if match:
                user = match.group('user')
                password = match.group('password')
                return user, password
        return None, None


    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.
        """
        if type(user_email) is str and type(user_pwd) is str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None
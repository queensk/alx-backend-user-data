#!/usr/bin/env python3
"""
class BasicAuth module
"""
from .auth import Auth
from re import fullmatch


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

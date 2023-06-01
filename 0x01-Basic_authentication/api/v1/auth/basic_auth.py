#!/usr/bin/env python3
"""
class BasicAuth module
"""
from .auth import Auth
from re import fullmatch
import base64
import binascii


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
git ad                return None
        return None

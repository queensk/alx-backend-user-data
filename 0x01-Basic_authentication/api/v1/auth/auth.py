#!/usr/bin/env python3
"""
Manage the API authentication.
"""
from flask import Flask, request
from typing import List, TypeVar

class Auth:
    """
    Manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False - path and excluded_paths will be used later.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None - request will be the Flask request object.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None - request will be the Flask request object.
        """
        return None

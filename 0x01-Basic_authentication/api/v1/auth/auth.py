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
        if path is None and excluded_paths in None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

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

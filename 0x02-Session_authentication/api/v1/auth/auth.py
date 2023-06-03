#!/usr/bin/env python3
"""
Manage the API authentication.
"""
from flask import Flask, request
from typing import List, TypeVar
from re import match
from os import getenv


class Auth:
    """
    Manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False - path and excluded_paths will be used later.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Request validation.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None - request will be the Flask request object.
        """
        return None

    def session_cookie(self, request=None) -> str:
        """
        returns a cookie value from a request
        """
        if request is None:
            cookie_name = getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)

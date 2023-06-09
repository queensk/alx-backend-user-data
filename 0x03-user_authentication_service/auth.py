#!/usr/bin/env python3
"""

"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> bytes:
    """Generate a salted hash of the input password using bcrypt

    Args:
        password (str): The input password string

    Returns:
        bytes: The salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


def _generate_uuid() -> str:
    """
    Generates a new UUID and returns it as a string.
    """
    return str(uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the provided email and password.

        Args:
            email (str): The user's email
            password (str): The user's password

        Returns:
            User: The created User object

        Raises:
            ValueError: If a user already exists with the provided email
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if the login credentials are valid.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Create a session for the user with the given email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id) -> Union[User, None]:
        """
        Get a user session
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy the session of the user with the given user_id.

        Args:
            user_id (int): The ID of the user.

        Returns:
            None
        """
        if user_id:
            self._db.update_user(user_id, session_id=None)
        return None

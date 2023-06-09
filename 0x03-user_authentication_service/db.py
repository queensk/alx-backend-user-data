#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError

from user import Base, User


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database

        Args:
            email (str): User's email
            hashed_password (str): User's hashed password

        Returns:
            User: The created User object
        """
        try:
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            user = None
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user in the database by keyword arguments

        Args:
            **kwargs: Arbitrary keyword arguments to filter the query

        Returns:
            User: The first matching User object

        Raises:
            NoResultFound: If no results are found
            InvalidRequestError: If wrong query arguments are passed
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user in the database by user_id and keyword arguments

        Args:
            user_id (int): The ID of the user to update
            **kwargs: Arbitrary keyword arguments to update the user's attributes

        Raises:
            NoResultFound: If no user is found with the given user_id
            ValueError: If an argument does not correspond to a user attribute
        """
        user = self.find_user_by(id=user_id)
        for attr, value in kwargs.items():
            if hasattr(User, attr):
                setattr(user, attr, value)
            else:
                raise ValueError()

        self._session.commit()

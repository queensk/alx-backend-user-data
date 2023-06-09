#!/usr/bin/env python3
"""
user model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
    user object Representation
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(256), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)

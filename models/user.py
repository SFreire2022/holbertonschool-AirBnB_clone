#!/usr/bin/python3
""" users class """


from models.base_model import BaseModel


class User(BaseModel):
    """ class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

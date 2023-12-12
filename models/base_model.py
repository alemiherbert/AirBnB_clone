#!/usr/bin/python3

"""
This is file contains the base class for the entire project
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """The base model for all the classes in AirBnB
    Attributes:
        id (str): A unique identifier for each user created
        created_at: timestamp at creation
        updated_at: timestamp at updation

    Methods:
        __str__: prints a string representation of the class (name, id)
                 creates a dictionary representation of the object
        save: update the current attributes with the current datetime
        to_dict: returns a dictionary values of the instance object
    """
    def __init__(self, *args, **kwargs):
        """Initialises public instance attributes
        Args:
            args: arguments
            kwargs: keyword arguments
        """
        DT_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(value, DT_FORMAT))
                elif key.startswith("id"):
                    setattr(self, key, str(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            models.storage.new(self)

        def __str__(self):
            """Returns a string representation of the class"""
            return f"[{self.__class__.__name__} {self.id} {self.__dict__}]"

        def save(self):
            """Updates the public instance variable `updated_at`
            with the current timestamp"""
            self.updated_at = datetime.utcnow()

        def to_dict(self):
            """Returns a dictionary containing the key-value
            pairs of a dictionary instance
            """
            output = {}
            for key, value in self.__dict__.items():
                if key in ("created_at", "updated_at"):
                    output[key] = value.isoformat()
                else:
                    output[key] = value
            output["__class__"] = self.__class__.__name__
            return output

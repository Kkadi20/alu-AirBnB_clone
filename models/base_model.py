#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """Base model for all classes in the AirBnB clone project"""

    def __init__(self):
        """Initialize a new instance with id and timestamps"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of all attributes, with ISO datetime format"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

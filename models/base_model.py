#!/usr/bin/python3
"""base model"""


<<<<<<< HEAD
=======
import json
>>>>>>> 0bce6b3e778025d8430e7bd65ad14cf28460cd56
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Base Model __init__ Method"""
<<<<<<< HEAD

        self.id = str(uuid4())
        self.name = name
        self.updated_at = self.created_at = datetime.now()

=======
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
>>>>>>> 0bce6b3e778025d8430e7bd65ad14cf28460cd56

    def __str__(self):
        """prints string representation of base"""

<<<<<<< HEAD
    return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
=======
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
>>>>>>> 0bce6b3e778025d8430e7bd65ad14cf28460cd56

    def save(self):
        """saves"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary"""

        return dict(self.__dict__,
                    __class__=self.__class__.__name__,
                    updated_at=self.updated_at.isoformat(),
                    created_at=self.created_at.isoformat())

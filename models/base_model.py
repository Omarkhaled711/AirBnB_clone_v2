#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime,
                        default=datetime.utcnow,
                        nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.utcnow,
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:

            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dict = self.to_dict()
        return '[{}] ({}) {}'.format(cls, self.id, dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state')
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage (models.storage)"""
        from models import storage
        storage.delete(self)

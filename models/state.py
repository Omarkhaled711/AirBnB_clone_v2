#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )

    # Note: If I were to use @property cities to return city list only with
    # Filestorage, and depend on cities relationship for when storage is DB
    # I would have to refactor the whole code base, so I did it like this
    # temporarly, after all the Database storage is the only one going for
    # production.
    def get_cities(self):
        """ Getter method to return the list of City objects
        regardless of the storage type"""
        from models import storage
        from models.city import City
        city_list = []
        for city in list(storage.all(City).values()):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

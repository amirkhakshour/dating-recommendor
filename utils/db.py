import pickle
from functools import cached_property
from abc import ABCMeta, abstractmethod

from . import settings
from .loading import import_string


class DBException(Exception):
    pass


class DBNotFoundException(DBException):
    pass


class IDB(metaclass=ABCMeta):

    @abstractmethod
    def _load_db(self):
        pass

    @cached_property
    def db(self):
        return self._load_db()

    @abstractmethod
    def get_by_id(self, _id):
        pass

    def process_item(self, profile):
        """Add profile processing here, e.g. adding vector field to the profile"""
        return profile

    @abstractmethod
    def __iter__(self):
        pass


class PickledDB(IDB):

    def __init__(self, db_path=None):
        self.db_path = db_path
        if self.db_path is None:
            self.db_path = settings.PROFILES_DB

    def _load_db(self):
        db = {}
        with open(self.db_path, 'rb') as file:
            items = pickle.load(file)
            for item in items:  # TODO handle file access error exceptions
                db[item['_id']] = self.process_item(item)
        return db

    def get_by_id(self, _id):
        try:
            return self.db[_id]
        except KeyError:
            raise DBNotFoundException("Given key not found in db: {}".format(_id))

    def __iter__(self):
        return iter(self.db.items())


def get_db():
    handler = import_string(settings.DB_HANDLER)
    return handler()


db = get_db()

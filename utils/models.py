import six
from abc import ABCMeta, abstractmethod
from functools import cached_property
from .db import db
from .misc import k_smallest_items, vectorize, cosine_similarity


class Model:
    _fields = []

    def __init__(self, *args, **kwargs):
        # Set the arguments
        for name in self._fields:
            if name in kwargs:
                setattr(self, name, kwargs.pop(name))


class IVectorModel(six.with_metaclass(ABCMeta, Model)):
    @abstractmethod
    def serialize(self):
        pass

    @cached_property
    def vector(self):
        _raw_data = {k: getattr(self, k, None) for k in self._fields}
        return vectorize(_raw_data)

    def k_nearest_neighbors_naive(self, capacity, method=cosine_similarity):
        """Naive implementation of K nearest neighbour functionality using cosine similarity."""
        container = k_smallest_items(capacity)
        k_nearest = []
        next(container)
        for _id, values in db:
            other_vector = vectorize(values)
            cos_sim = method(self.vector, other_vector)
            k_nearest = container.send((cos_sim, values))
        container.close()
        k_nearest.sort(key=lambda x: x[0])
        return [x[-1] for x in k_nearest]


class Profile(IVectorModel):
    _fields = ['_id', 'name', 'surname']
    _serialize_fields = ['_id', 'name', 'surname', 'vector']

    def serialize(self):
        return {k: getattr(self, k, None) for k in self._serialize_fields}

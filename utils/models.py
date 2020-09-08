class Model:
    _fields = []

    def __init__(self, *args, **kwargs):
        # Set the arguments
        for name in self._fields:
            if name in kwargs:
                setattr(self, name, kwargs.pop(name))

class Empty:
    def __repr__(self):
        return "<Empty>"


class Object(object):
    def __init__(self, attributes: dict):
        for key, value in attributes.items():
            setattr(self, key, value)


class Array(list):
    def __init__(self, *args):
        super().__init__(args)

    @property
    def length(self):
        return len(self)

    @length.setter
    def length(self, new_length):
        if new_length <= len(self):
            for i in range(new_length):
                self.pop(i)
        if new_length >= len(self):
            difference = new_length - len(self)
            for _ in range(difference):
                self.append(Empty())

    def push(self, item):
        super().append(item)

    def shift(self):
        first_element = self[0]
        self.remove(first_element)


class String(str):
    pass


class Tuple(tuple):
    pass

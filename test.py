import importlib
import json
import math

import yaml


class DumpMixin:
    def get_data(self):
        return self.__dict__

    def set_data(self, pod_data):
        self.__dict__.update(pod_data)

    def get_object_data(self):
        metadata = (
            type(self).__module__,  # self.__class__.__module__
            type(self).__name__,
        )

        obj = (*metadata, self.get_data())

        return obj


class Serializer:
    @staticmethod
    def from_object_data(serialized_data):
        module, class_name, data = serialized_data
        klass = getattr(importlib.import_module(module), class_name)
        obj = klass(**data)
        return obj


class A(DumpMixin):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Parser:
    @staticmethod
    def format(value):
        raise NotImplemented('Not impemented')

    @staticmethod
    def parse(data):
        raise NotImplemented('Not impemented')


class JsonParser(Parser):
    @staticmethod
    def format(value):
        return json.dumps(value)

    @staticmethod
    def parse(data):
        return json.loads(data)


class YamlParser(Parser):
    @staticmethod
    def format(value):
        return yaml.dump(value)

    @staticmethod
    def parse(data):
        return yaml.load(data)


class FileDumper:
    serializer = Serializer
    parser = JsonParser

    @classmethod
    def create_from_file(cls, filepath):
        with open(filepath) as f:
            data = cls.parser.parse(f.read())
            instance = cls.serializer.from_object_data(data)
        return instance

    @classmethod
    def save_to_file(cls, filepath, obj):
        with open(filepath, 'w+') as f:
            serialized = cls.parser.format(obj.get_object_data())
            f.write(serialized)


#     @staticmethod
#     def save_to_file(filepath, obj):
#         with open(filepath, 'w+') as f:
#             serialized = FileDumper.parser.format(obj.get_object_data())
#             f.write(serialized)


class JsonFileDumper(FileDumper):
    parser = JsonParser


class YamlFileDumper(FileDumper):
    parser = YamlParser


class Shape(DumpMixin):  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):
    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


r = Parallelogram(0, 0, 10, 20, 45)
JsonFileDumper.save_to_file('scene.json', r)  # FileDumper.save_to_file(cls : FileDumper)
r2 = JsonFileDumper.create_from_file('scene.json')

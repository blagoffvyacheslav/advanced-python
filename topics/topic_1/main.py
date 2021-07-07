from marshmallow import Schema, fields

def my_dataclass():
    def _wrapper(clazz):
        match = {}
        name = clazz.__name__
        attrs = clazz.__annotations__
        for key, value in attrs.items():
            match[key] = Schema.TYPE_MAPPING[attrs[key]]()
        clazz.schema = type(name, (Schema, ), match)
        return clazz
    return _wrapper

@my_dataclass()
class User:
    id: int
    username: str



print(User.schema().load({'username': 'Vyacheslav', 'id': 1}))

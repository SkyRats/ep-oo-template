from typing import Any


def get_attr(obj: Any, attr_name: str) -> Any:
    possible_attr_names = [attr_name, attr_name.capitalize(), attr_name.lower()]
    possible_prefixes = ['{}', '_{}', '__{}']
    # Check if obj has any combination of attr_names and prefixes
    # and return the first one that exists
    for possible_attr_name in possible_attr_names:
        for possible_prefix in possible_prefixes:
            possible_attr_name = possible_prefix.format(possible_attr_name)
            print(possible_attr_name)
            if hasattr(obj, possible_attr_name):
                return getattr(obj, possible_attr_name)

    raise AttributeError(f'{obj} has no attribute whose name '
                        +f'contains {attr_name}')

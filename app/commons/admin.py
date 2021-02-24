from typing import Callable


def short_description(text: str):
    """
    Example:

        >>> @short_description('full name')
        ... def get_full_name(self):
        ...     return ...
    """
    def decor(f: Callable):
        f.short_description = text
        return f

    return decor

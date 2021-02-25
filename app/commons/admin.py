from typing import Callable, List, Tuple, Optional, Dict


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


class AddFieldsetsMixin:
    """
    The idea was taken from `django.contrib.auth.admin.UserAdmin`
    """
    add_fieldsets: List[
        Tuple[
            Optional[str],
            Dict[str, List[str]]
        ]
    ]

    def get_fieldsets(self, request, obj=None):
        if obj is None:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)  # noqa

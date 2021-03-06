# Stubs for django.core.paginator (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import collections

class InvalidPage(Exception): ...
class PageNotAnInteger(InvalidPage): ...
class EmptyPage(InvalidPage): ...

class Paginator:
    object_list = ... # type: Any
    per_page = ... # type: Any
    orphans = ... # type: Any
    allow_empty_first_page = ... # type: Any
    def __init__(self, object_list, per_page, orphans=0, allow_empty_first_page=True): ...
    def validate_number(self, number): ...
    def page(self, number): ...
    count = ... # type: Any
    num_pages = ... # type: Any
    page_range = ... # type: Any

QuerySetPaginator = ... # type: Any

class Page(collections.Sequence):
    object_list = ... # type: Any
    number = ... # type: Any
    paginator = ... # type: Any
    def __init__(self, object_list, number, paginator): ...
    def __len__(self): ...
    def __getitem__(self, index): ...
    def has_next(self): ...
    def has_previous(self): ...
    def has_other_pages(self): ...
    def next_page_number(self): ...
    def previous_page_number(self): ...
    def start_index(self): ...
    def end_index(self): ...

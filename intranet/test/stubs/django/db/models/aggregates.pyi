# Stubs for django.db.models.aggregates (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.db.models.expressions import Func

class Aggregate(Func):
    contains_aggregate = ... # type: Any
    name = ... # type: Any
    def resolve_expression(self, query=None, allow_joins=True, reuse=None, summarize=False, for_save=False): ...
    @property
    def default_alias(self): ...
    def get_group_by_cols(self): ...

class Avg(Aggregate):
    function = ... # type: Any
    name = ... # type: Any
    def __init__(self, expression, **extra): ...
    def as_oracle(self, compiler, connection): ...

class Count(Aggregate):
    function = ... # type: Any
    name = ... # type: Any
    template = ... # type: Any
    def __init__(self, expression, distinct=False, **extra): ...
    def convert_value(self, value, expression, connection, context): ...

class Max(Aggregate):
    function = ... # type: Any
    name = ... # type: Any

class Min(Aggregate):
    function = ... # type: Any
    name = ... # type: Any

class StdDev(Aggregate):
    name = ... # type: Any
    function = ... # type: Any
    def __init__(self, expression, sample=False, **extra): ...
    def convert_value(self, value, expression, connection, context): ...

class Sum(Aggregate):
    function = ... # type: Any
    name = ... # type: Any
    def as_oracle(self, compiler, connection): ...

class Variance(Aggregate):
    name = ... # type: Any
    function = ... # type: Any
    def __init__(self, expression, sample=False, **extra): ...
    def convert_value(self, value, expression, connection, context): ...

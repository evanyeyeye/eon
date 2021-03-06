# Stubs for fabric.context_managers (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def documented_contextmanager(func): ...
def show(*groups): ...
def hide(*groups): ...
def settings(*args, **kwargs): ...
def cd(path): ...
def lcd(path): ...
def path(path, behavior: str = ...): ...
def prefix(command): ...
def char_buffered(pipe): ...
def shell_env(**kw): ...
def remote_tunnel(remote_port, local_port: Optional[Any] = ..., local_host: str = ..., remote_bind_address: str = ...): ...

quiet = ...  # type: Any
warn_only = ...  # type: Any

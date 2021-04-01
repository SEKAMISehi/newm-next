from __future__ import annotations
from typing import TypeVar, Optional, Callable

import pathlib
import importlib
import logging
import sys
import os

_provider = {}
_consumer = {}

logger = logging.getLogger(__name__)


class _ConfiguredValue:
    def __init__(self, name, value, default):
        self._name = name
        self._value = None
        self._default = default

        self.update(value)

    def update(self, value):
        self._value = value if value is not None else self._default

    def __call__(self):
        return self._value

    def __str__(self):
        return "%-60s %-40s %s" % (self._name, self._value, ("(default: %s)" % self._default) if self._default != self._value else "")

def _update_config(at_c, at_p):
    if isinstance(at_c, _ConfiguredValue):
        at_c.update(at_p)
    else:
        if isinstance(at_c, dict):
            for k in at_c.keys():
                _update_config(at_c[k], at_p[k] if (at_p is not None and k in at_p) else None)
        else:
            logger.warn("Config: Unexpected")

def print_config(at_c=None):
    if at_c is None:
        at_c = _consumer

    if isinstance(at_c, _ConfiguredValue):
        return str(at_c)
    else:
        if isinstance(at_c, dict):
            return "\n".join([print_config(at_c[k]) for k in at_c.keys()])
        else:
            logger.warn("Config: Unexpected")

def load_config(fallback: bool=True) -> None:
    global _provider

    home = os.environ['HOME'] if 'HOME' in os.environ else '/'
    path = pathlib.Path(home) / '.config' / 'newm' / 'config.py'
    path_default = pathlib.Path(__file__).parent.absolute() / 'default_config.py'

    if not path.is_file():
        path = pathlib.Path('/etc') / 'newm' / 'config.py'

    if not path.is_file():
        path = path_default

    logger.info("Loading config at %s", path)

    def load(path):
        module = path.stem

        try:
            del sys.modules[module]
        except KeyError:
            pass

        sys.path.insert(0, str(path.parent))
        return importlib.import_module(module).__dict__

    try:
        _provider = load(path)
    except:
        if fallback:
            logger.exception("Error loading config - falling back to default")
            try:
                _provider = load(path_default)
            except:
                logger.exception("Error loading default config")
                _provider = {}
        else:
            logger.exception("Error loading config")

    _update_config(_consumer, _provider)


T = TypeVar('T')
def configured_value(path, default: Optional[T]=None) -> Callable[[], T]:
    global _consumer

    result = None
    try:
        v = _provider
        for k in path.split("."):
            v = v[k]

        result = v
    except KeyError:
        pass

    c = _consumer
    for k in path.split(".")[:-1]:
        try:
            c = c[k]
        except KeyError:
            c[k] = {}
            c = c[k]

    k = path.split(".")[-1]
    if k in c and isinstance(c[k], _ConfiguredValue):
        return c[k]

    result = _ConfiguredValue(path, result, default)
    c[k] = result
    return result



if __name__ == '__main__':
    scale = configured_value('output_scale', 1.0)
    pywm = configured_value('pywm', {})
    while True:
        print("Scale is %f" % scale())
        print("PyWM is %s" % pywm())
        input("Update? ")
        load_config()

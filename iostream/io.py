import sys
from . import istream
from . import ostream

pin = istream(sys.stdin)
pout = ostream(sys.stdout)
perr = ostream(sys.stderr)
__check_if_iostream_missing__ = False

def set_io_check(args=True) -> None:
    global __check_if_iostream_missing__
    if not type(args) == bool:
        raise ValueError('args for set_io_check() must me boolean')
    __check_if_iostream_missing__ = args

def __iostream_checker__(frame, event, args) -> None:
    if not __check_if_iostream_missing__:
        return
    if not isinstance(pin, istream):
        raise ValueError('pin needs to always be type istream')
    if not isinstance(pout, ostream):
        raise ValueError('pout needs to always be type ostream')
    if not isinstance(perr, ostream):
        raise ValueError('perr needs to always be type ostream')
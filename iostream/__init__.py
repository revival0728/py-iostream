import sys
from .istream import istream
from .ostream import ostream
from .io import pin
from .io import pout
from .io import perr


sys.settrace(io.__iostream_checker__)  # need fix
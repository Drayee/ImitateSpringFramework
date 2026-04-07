import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
os.chdir(os.sep.join(current_dir.split(os.sep)[:-1]+["src"]))
from resource import logging
from public_modules import *

__all__ = [
    "controller",
    "auto_inject",
    "Service",
]

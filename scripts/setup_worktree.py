"""Check the existing CPU/static test runtime without touching services or models."""
import sys

import numpy
import torch

if sys.version_info < (3, 10):
    raise SystemExit("Python 3.10+ is required")
print(f"Ready: Python {sys.version.split()[0]}, torch {torch.__version__}, numpy {numpy.__version__}")

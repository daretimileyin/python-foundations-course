# Lets pytest import modules from this folder (e.g. `from calculator import add`)
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

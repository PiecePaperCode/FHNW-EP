import os
from pathlib import Path

Basisroutine = Path(os.path.dirname(__file__)) / 'Basisroutine.txt'

def read_Basisroutine():
    with open(Basisroutine) as file:
        return file.read()

def write_Basisroutine(text):
    with open(Basisroutine, 'w') as file:
        file.write(text)
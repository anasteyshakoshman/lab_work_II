from pathlib import Path
import os
from os.path import isfile

MAX_SIZE = 512

encode = {'@':1, '_':-1}

def parse(dir):
    shapes_files = []
    for filename in os.listdir(dir):
        path = os.path.join(dir, filename)
        if Path(path).suffix == '.txt':
            shapes_files.append(path)
    return [parse_shape(path) for path in shapes_files]


def parse_shape(path):
    with open(path) as f:
        shape = f.read(MAX_SIZE)
        shape = shape.replace('\n', '')
        return [encode[a] for a in shape]
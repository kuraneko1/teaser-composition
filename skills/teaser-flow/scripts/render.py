from pathlib import Path
import json
from core import run
from scene import draw, DEFAULT
if __name__ == '__main__':
    run(draw, DEFAULT, json.loads((Path(__file__).parent / 'presets.json').read_text()))

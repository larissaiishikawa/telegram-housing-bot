import json
from pathlib import Path

FILE = Path("data/seen.json")

def load_seen():
    if not FILE.exists():
        return set()

    return set(json.loads(FILE.read_text()))

def save_seen(items):
    FILE.parent.mkdir(exist_ok=True)

    FILE.write_text(
        json.dumps(list(items))
    )

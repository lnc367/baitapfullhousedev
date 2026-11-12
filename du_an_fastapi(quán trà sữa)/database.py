import json
from pathlib import Path

DATA_FILE = Path("data.json")

DEFAULT_DATA = {
    "menu": [
        {"id": 1, "name": "Trà sữa trân châu", "price": 30000, "category":
        "tra-sua"},
        {"id": 2, "name": "Trà đào cam sả", "price": 35000, "category":
        "tra-trai-cay"},
        {"id": 3, "name": "Matcha latte", "price": 40000, "category": "tra-sua"},
    ],
    "orders": [],
}

def load_data():
    if not DATA_FILE.exists():
        save_data(DEFAULT_DATA)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)   
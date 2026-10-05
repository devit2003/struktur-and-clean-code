import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Root JSON harus berupa list.")

    for index, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(
                f"Item pada index {index} harus berupa object/dict."
            )

    return data
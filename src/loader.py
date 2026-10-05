import json
from pathlib import Path
from typing import Any


class InvalidDocumentStructureError(Exception):
    """Raised when JSON structure does not match the expected format."""


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def validate_documents(data: Any) -> list[dict[str, Any]]:
    if not isinstance(data, list):
        raise InvalidDocumentStructureError(
            "Root JSON harus berupa list."
        )

    for index, item in enumerate(data):
        if not isinstance(item, dict):
            raise InvalidDocumentStructureError(
                f"Item pada index {index} harus berupa object/dict."
            )

    return data
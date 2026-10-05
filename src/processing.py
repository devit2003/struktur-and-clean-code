from typing import Any


def clean_texts(documents: list[dict[str, Any]]) -> list[str]:
    cleaned_texts = []

    for document in documents:
        text = document.get("text")

        if not isinstance(text, str) or not text.strip():
            continue

        cleaned_texts.append(text.lower().strip())

    return cleaned_texts
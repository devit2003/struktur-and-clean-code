import argparse
import json
import logging
from pathlib import Path

from loader import load_json
from processing import clean_texts


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Load and clean documents from a JSON file."
    )

    parser.add_argument(
        "path",
        type=Path,
        help="Path ke file JSON",
    )

    args = parser.parse_args()

    try:
        documents = load_json(args.path)
    except FileNotFoundError:
        logger.error("File tidak ditemukan: %s", args.path)
        return
    except json.JSONDecodeError:
        logger.error("JSON tidak valid: %s", args.path)
        return

    cleaned_texts = clean_texts(documents)

    logger.info("Jumlah dokumen: %d", len(cleaned_texts))

    for text in cleaned_texts:
        print(text)


if __name__ == "__main__":
    main()
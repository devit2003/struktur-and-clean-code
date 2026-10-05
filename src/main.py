import argparse
import json
import logging
import sys
from pathlib import Path

from loader import (
    InvalidDocumentStructureError,
    load_json,
    validate_documents,
)
from processing import clean_texts


logger = logging.getLogger(__name__)


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )


def main() -> None:
    setup_logging()

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
        data = load_json(args.path)
        documents = validate_documents(data)

    except FileNotFoundError:
        logger.error("File tidak ditemukan: %s", args.path)
        sys.exit(1)

    except json.JSONDecodeError:
        logger.error("JSON tidak valid: %s", args.path)
        sys.exit(1)

    except InvalidDocumentStructureError as error:
        logger.error("Struktur JSON tidak valid: %s", error)
        sys.exit(1)

    cleaned_texts = clean_texts(documents)

    if not cleaned_texts:
        logger.warning("Tidak ada dokumen untuk diproses.")
        return

    logger.info("Jumlah dokumen: %d", len(cleaned_texts))

    for text in cleaned_texts:
        print(text)


if __name__ == "__main__":
    main()
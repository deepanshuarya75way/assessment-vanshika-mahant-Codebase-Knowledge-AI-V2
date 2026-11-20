
import json
from pathlib import Path
from typing import Any, Dict, List

BOOKMARK_FILE = Path("data") / "bookmarks.json"


def load_bookmarks() -> List[Dict[str, Any]]:
    """Load saved bookmarks from JSON."""

    if not BOOKMARK_FILE.exists():
        return []

    try:
        content = BOOKMARK_FILE.read_text(encoding="utf-8").strip()

        if not content:
            return []

        bookmarks = json.loads(content)

        if not isinstance(bookmarks, list):
            return []

        return bookmarks

    except json.JSONDecodeError:
        return []


def save_bookmark(bookmark: Dict[str, Any]) -> None:
    """Save a new bookmark permanently."""

    bookmarks = load_bookmarks()
    bookmarks.append(bookmark)

    BOOKMARK_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(BOOKMARK_FILE, "w", encoding="utf-8") as f:
        json.dump(bookmarks, f, indent=4, ensure_ascii=False)

def update_bookmark(index: int, note: str, tags: List[str]) -> None:
    """Update note and tags for an existing bookmark."""
    bookmarks = load_bookmarks()

    if 0 <= index < len(bookmarks):
        bookmarks[index]["note"] = note
        bookmarks[index]["tags"] = tags

        BOOKMARK_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(BOOKMARK_FILE, "w", encoding="utf-8") as f:
            json.dump(bookmarks, f, indent=4, ensure_ascii=False)

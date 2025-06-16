import os
import orjson
from typing import Any, Dict, List

# Default path for JSON sink (in backend root)
BASE_PATH = os.getcwd()
SUBMISSIONS_FILE = os.path.join(BASE_PATH, 'submissions.json')

def save_submission(data: Dict[str, Any]) -> None:
    """
    Append a form submission dict to a JSON file. Creates the file if it doesn't exist.
    Prevents duplicates by checking existing entries.
    """
    # Load existing submissions
    if os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, 'rb') as f:
            try:
                submissions: List[Any] = orjson.loads(f.read())
            except Exception:
                submissions = []
    else:
        submissions = []

    # Append new entry only if not already present
    if data in submissions:
        return
    submissions.append(data)
    with open(SUBMISSIONS_FILE, 'wb') as f:
        # indent for readability
        f.write(orjson.dumps(submissions, option=orjson.OPT_INDENT_2))

def load_submissions():
    """
    Read and return all form submissions from the JSON file.
    Returns an empty list if file doesn't exist or on parse errors.
    """
    if os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, 'rb') as f:
            try:
                return orjson.loads(f.read())
            except Exception:
                return []
    return []

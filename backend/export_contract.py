"""Export the API contract; run `uv run python export_contract.py` from backend/."""

import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "backend"))
from app.main import app  # noqa: E402

target = root / "contracts" / "openapi.json"
content = json.dumps(app.openapi(), indent=2, sort_keys=True) + "\n"
if "--check" in sys.argv:
    if not target.exists() or target.read_text(encoding="utf-8") != content:
        raise SystemExit(
            "OpenAPI contract is stale. Run backend/export_contract.py and regenerate TypeScript."
        )
else:
    target.parent.mkdir(exist_ok=True)
    target.write_text(content, encoding="utf-8")

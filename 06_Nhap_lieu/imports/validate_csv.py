"""Validate CSV structure and basic types; business rules require server dry-run."""

import argparse
import csv
import json
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path


def validate(directory):
    """Return (rows_checked, errors). A subset of known templates is allowed."""
    directory = Path(directory)
    errors = []
    count = 0
    if not directory.is_dir():
        return 0, [[str(directory), 0, "DIRECTORY", "Directory does not exist"]]

    spec = json.loads(
        Path(__file__).with_name("template_manifest.json").read_text(encoding="utf-8")
    )
    templates = {t["name"] + ".csv": t for t in spec["templates"]}
    paths = sorted(directory.glob("*.csv"))
    if not paths:
        return 0, [[str(directory), 0, "FILES", "No CSV files found"]]

    for path in paths:
        template = templates.get(path.name)
        if template is None:
            errors.append([path.name, 0, "FILE", "Unknown template filename"])
            continue
        expected = [column["name"] for column in template["columns"]]
        reader = None
        try:
            with path.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.reader(stream, strict=True)
                if next(reader, None) != expected:
                    errors.append([path.name, 1, "HEADER", "Headers or order differ"])
                    continue
                for row in reader:
                    line = reader.line_num
                    if not row or not any(value.strip() for value in row):
                        continue
                    count += 1
                    if len(row) != len(expected):
                        errors.append([path.name, line, "ROW", "Wrong number of columns"])
                        continue
                    for column, raw_value in zip(template["columns"], row):
                        value = raw_value.strip()
                        if not value:
                            if column["required"]:
                                errors.append([path.name, line, column["name"], "REQUIRED"])
                            continue
                        try:
                            kind = column["type"]
                            if kind == "decimal":
                                if not Decimal(value).is_finite() or "," in value:
                                    raise ValueError
                            elif kind == "integer":
                                if str(int(value)) != value:
                                    raise ValueError
                            elif kind == "boolean":
                                if value.upper() not in {"TRUE", "FALSE"}:
                                    raise ValueError
                            elif kind == "date":
                                if date.fromisoformat(value).isoformat() != value:
                                    raise ValueError
                            elif kind == "datetime":
                                if datetime.fromisoformat(value.replace("Z", "+00:00")).tzinfo is None:
                                    raise ValueError
                        except (ValueError, InvalidOperation):
                            errors.append([path.name, line, column["name"], "INVALID_TYPE"])
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append([path.name, reader.line_num if reader else 0, "FILE", str(exc)])
    return count, errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Directory containing named CSV templates")
    args = parser.parse_args(argv)
    count, errors = validate(args.directory)
    print(json.dumps({
        "rows_checked": count,
        "errors": errors,
        "scope": "Basic structure/types only; use server dry-run for business rules.",
    }, ensure_ascii=False, indent=2))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())

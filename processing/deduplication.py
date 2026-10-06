import re

def normalize_key(value):
    value = str(value or "").lower().strip()
    return re.sub(r"\s+", " ", value)

def deduplicate(records):
    seen = set()
    unique = []
    duplicates = []

    for record in records:
        key = (
            normalize_key(record.get("source")),
            normalize_key(record.get("name_or_title")),
            normalize_key(record.get("author"))
        )

        if key in seen:
            duplicates.append(record)
        else:
            seen.add(key)
            unique.append(record)

    return unique, duplicates

def validate_record(record):
    errors = []

    if not record.get("source"):
        errors.append("missing source")
    if not record.get("name_or_title"):
        errors.append("missing title")
    if not record.get("source_url"):
        errors.append("invalid URL")

    if record.get("price") != "":
        if not isinstance(record["price"], (int, float)) or record["price"] < 0:
            errors.append("invalid price")

    if record.get("rating") != "":
        if record["rating"] not in range(1, 6):
            errors.append("invalid rating")

    return errors

def validate_records(records):
    valid = []
    rejected = []

    for record in records:
        errors = validate_record(record)
        if errors:
            record["validation_errors"] = "; ".join(errors)
            rejected.append(record)
        else:
            valid.append(record)

    return valid, rejected

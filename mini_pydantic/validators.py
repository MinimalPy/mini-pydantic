from .exceptions import ValidationError

def validate(value, expected_type):
    if hasattr(expected_type, "__origin__") and expected_type.__origin__ is list:
        if not isinstance(value, list):
            raise ValidationError(f"Expected list, got {type(value).__name__}")

        item_type = expected_type.__args__[0]

        return [
            validate(item, item_type)
            for item in value
        ]

    if isinstance(value, expected_type):
        return value

    try:
        if expected_type in (int, float, str, bool):
            return expected_type(value)
    except (ValueError, TypeError):
        pass

    raise ValidationError(
        f"Expected {expected_type}, got {type(value).__name__}"
    )
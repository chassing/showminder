from django import template

register = template.Library()


@register.filter
def split(value: str, sep: str = ",") -> list[str]:
    """Split a string by separator and strip whitespace."""
    if not value:
        return []
    return [item.strip() for item in value.split(sep)]

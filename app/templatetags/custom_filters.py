from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def truncate_rich_text(value, arg):
    """Truncates rich text field to the specified number of words."""
    if not value:
        return ''
    plain_text = strip_tags(value)  # Remove HTML tags
    truncated_text = ' '.join(plain_text.split()[:arg])  # Truncate to specified number of words
    return truncated_text + '...' if len(plain_text.split()) > arg else plain_text

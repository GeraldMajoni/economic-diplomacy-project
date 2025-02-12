# reports/templatetags/math_extras.py

from django import template

register = template.Library()

@register.filter
def variance(baseline, actual):
    """
    Calculates the variance percentage as ((actual - baseline) / baseline) * 100.
    Returns None if baseline is zero or if conversion fails.
    """
    try:
        baseline = float(baseline)
        actual = float(actual)
        if baseline == 0:
            return None
        return ((actual - baseline) / baseline) * 100
    except (ValueError, TypeError):
        return None

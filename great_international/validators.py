import re

from django.core.exceptions import ValidationError


def validate_lat_long(value):
    if re.match(r'^(-|\+)?\d{1,3}(\.\d+)?\s*,\s*(-|\+)?\d{1,3}(\.\d+)?$', value.strip()) is None:
        raise ValidationError('Invalid latitude/longitude.')

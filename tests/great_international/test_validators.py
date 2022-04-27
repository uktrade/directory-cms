import pytest
from django.core.exceptions import ValidationError

from great_international.validators import validate_lat_long


@pytest.mark.django_db
@pytest.mark.parametrize(
    'value, raise_expected',
    (
        ('51.123456, -2.345678', False),
        (' 51.123456  , -2.345678  ', False),
        ('+51.123456, +1.1', False),
        ('  51.123456,   -2.345678  ', False),
        ('31.123456,2.345678', False),
        ('50, 2', False),
        ('50., 2.', True),
        ('50', True),
        ('50º N, 2º W', True),
        ('Not even trying', True),
    )
)
def test_validate_lat_long(value, raise_expected):
    try:
        validate_lat_long(value)
    except ValidationError:
        if not raise_expected:
            pytest.fail(f'Expected {value} to pass validation, but it failed')
    else:
        if raise_expected:
            pytest.fail(f'Expected {value} to fail validation, but it passed')

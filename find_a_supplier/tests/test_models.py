import pytest

from core.fields import APIHyperlinkField
from find_a_supplier import models


@pytest.mark.parametrize('model', (
    models.IndustryPage, models.IndustryArticlePage
))
def test_url_api_field(model):
    fields = {field.name: field for field in model.api_fields}

    assert isinstance(fields['url'], APIHyperlinkField)

import pytest

from core.fields import APIMetaField
from find_a_supplier import models


@pytest.mark.parametrize('model', (
    models.IndustryPage, models.IndustryArticlePage, models.IndustryLandingPage
))
def test_url_api_field(model):
    fields = {field.name: field for field in model.api_fields}

    assert isinstance(fields['meta'], APIMetaField)


@pytest.mark.django_db
def test_industries_page_published_url_field():
    instance = models.IndustryLandingPage()

    assert instance.published_url == (
        'http://supplier.trade.great:8005/industries/'
    )

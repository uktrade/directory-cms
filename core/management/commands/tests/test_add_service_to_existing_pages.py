import pytest
from django.core.management import call_command

from core.models import Service
from find_a_supplier.tests.factories import LandingPageFactory


@pytest.mark.django_db
def test_add_service_to_existing_pages():
    page = LandingPageFactory()
    Service.objects.all()  # service entry is create when the page is created
    call_command('add_service_to_existing_pages')
    assert Service.objects.filter(page=page).exists()

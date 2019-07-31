import pytest

from invest import serializers
from tests.invest import factories


@pytest.mark.django_db
def test_high_potential_opportunity_form_page_serializer():
    instance = factories.HighPotentialOpportunityFormPageFactory()

    serializer = serializers.HighPotentialOpportunityFormPageSerializer(
        instance
    )

    assert serializer.data['full_name'] == {
        'label': instance.full_name_label,
        'help_text': instance.full_name_help_text,
    }
    assert serializer.data['role_in_company'] == {
        'label': instance.role_in_company_label,
        'help_text': instance.role_in_company_help_text,
    }
    assert serializer.data['email_address'] == {
        'label': instance.email_address_label,
        'help_text': instance.email_address_help_text,
    }
    assert serializer.data['phone_number'] == {
        'label': instance.phone_number_label,
        'help_text': instance.phone_number_help_text,
    }
    assert serializer.data['company_name'] == {
        'label': instance.company_name_label,
        'help_text': instance.company_name_help_text,
    }
    assert serializer.data['website_url'] == {
        'label': instance.website_url_label,
        'help_text': instance.website_url_help_text,
    }
    assert serializer.data['country'] == {
        'label': instance.country_label,
        'help_text': instance.country_help_text,
    }
    assert serializer.data['company_size'] == {
        'label': instance.company_size_label,
        'help_text': instance.company_size_help_text,
    }
    assert serializer.data['opportunities'] == {
        'label': instance.opportunities_label,
        'help_text': instance.opportunities_help_text,
    }
    assert serializer.data['comment'] == {
        'label': instance.comment_label,
        'help_text': instance.comment_help_text,
    }

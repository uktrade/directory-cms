import pytest
from find_a_supplier.serializers import IndustryPageSerializer


@pytest.mark.django_db
def test_base_page_serializer(page, rf):
    page.slug = 'test-slug'
    page.pk = 4

    serializer = IndustryPageSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert serializer.data['id'] == page.id
    assert serializer.data['seo_title'] == page.seo_title
    assert serializer.data['search_description'] == page.search_description
    assert 'meta' in serializer.data  # meta content tested in another test
    assert serializer.data['full_url'] == page.full_url
    assert serializer.data['full_path'] == page.full_path
    assert serializer.data['last_published_at'] == page.last_published_at
    assert serializer.data['title'] == page.title
    assert serializer.data['page_type'] == 'IndustryPage'

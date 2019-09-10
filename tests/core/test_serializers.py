import pytest
from great_international.serializers import CapitalInvestContactFormSuccessPageSerializer, \
    InternationalArticlePageSerializer
from tests.great_international.factories import CapitalInvestContactFormPageFactory, \
    CapitalInvestContactFormSuccessPageFactory, InternationalArticlePageFactory


@pytest.mark.django_db
def test_base_page_serializer(rf, international_root_page):
    page = InternationalArticlePageFactory(slug='test-slug', parent=international_root_page)

    serializer = InternationalArticlePageSerializer(
        instance=page,
        context={'request': rf.get('/')}
    )

    assert serializer.data['id'] == page.id
    assert serializer.data['seo_title'] == page.seo_title
    assert serializer.data['search_description'] == page.search_description
    assert 'meta' in serializer.data  # meta content tested in another test
    assert serializer.data['full_url'] == page.full_url
    assert serializer.data['full_path'] == page.full_path
    assert serializer.data['title'] == page.title
    assert serializer.data['page_type'] == 'InternationalArticlePage'


@pytest.mark.django_db
def test_tree_based_breadcrumbs_for_base_page_serializer(
        rf, international_root_page
):
    form_page = CapitalInvestContactFormPageFactory(
        slug='contact',
        title_en_gb='form-title',
        breadcrumbs_label='breadcrumbs',
        parent=international_root_page
    )

    success_page = CapitalInvestContactFormSuccessPageFactory(
        slug='success',
        title_en_gb="success-title",
        parent=form_page
    )

    success_serializer = CapitalInvestContactFormSuccessPageSerializer(
        instance=success_page,
        context={'request': rf.get('/')}
    )

    assert success_serializer.data['tree_based_breadcrumbs'][0]['title'] == 'breadcrumbs'
    assert success_serializer.data['tree_based_breadcrumbs'][1]['title'] == 'success-title'

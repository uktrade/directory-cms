import pytest
from django.core.management import call_command

from tests.export_readiness.factories import ArticlePageFactory


@pytest.mark.django_db
def test_enable_tree_based_routing_service_name_specified(root_page):
    article = ArticlePageFactory(parent=root_page)

    assert article.uses_tree_based_routing is False

    call_command('enable_tree_based_routing', '--servicename=domestic')
    article.refresh_from_db()

    assert article.uses_tree_based_routing is True


@pytest.mark.django_db
def test_enable_tree_based_routing_all_pages(root_page):
    article = ArticlePageFactory(parent=root_page)

    assert article.uses_tree_based_routing is False

    call_command('enable_tree_based_routing')
    article.refresh_from_db()

    assert article.uses_tree_based_routing is True

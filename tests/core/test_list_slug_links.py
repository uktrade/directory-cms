from io import StringIO

import pytest

from django.core.management import call_command
from django.urls import reverse

from tests.export_readiness.factories import ArticlePageFactory, CountryGuidePageFactory


@pytest.mark.django_db
def test_list_slug_links(root_page):
    stdout = StringIO()

    guide = CountryGuidePageFactory.create(
        slug='bar',
        parent=root_page,
        section_one_body=f'[things](pk:{root_page.pk}) are nice',
    )
    article = ArticlePageFactory.create(
        parent=root_page,
        article_body_text=f'[things](slug:{guide.slug}) are good',
    )

    call_command('list_slug_links', stdout=stdout)
    stdout.seek(0)
    urls = stdout.read()

    assert reverse('wagtailadmin_pages:edit', args=(article.pk,)) in urls
    assert reverse('wagtailadmin_pages:edit', args=(guide.pk,)) not in urls

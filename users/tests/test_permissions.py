import pytest
from django.urls import reverse
from rest_framework import status

import export_readiness.tests.factories as exred_factories


@pytest.mark.CMS_837
@pytest.mark.django_db
def test_branch_moderators_should_see_pages_only_from_their_branch(
    branch_moderator_factory, root_page
):
    branch_1 = branch_moderator_factory.get(root_page)
    branch_2 = branch_moderator_factory.get(root_page)

    # This reproduces Wagtail's Admin call to list pages in
    # the 'Pages' menu.
    # User can only see pages that are child of requested page to which
    # he has access to
    resp_1 = branch_1.client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_1.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_1.status_code == status.HTTP_200_OK
    assert resp_1.json()['meta']['total_count'] == 1
    assert resp_1.json()['items'][0]['id'] == branch_1.article.pk

    # This reproduces situation when User navigates down the 'Pages' menu
    # User shouldn't see any child pages of an article as it doesn't have any
    resp_2 = branch_1.client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_1.article.pk}&for_explorer=1'  # NOQA
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert resp_2.json()['meta']['total_count'] == 0
    assert not resp_2.json()['items']

    # Wagtail API allows users to list pages that belong to different group!
    resp_3 = branch_1.client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_2.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_3.status_code == status.HTTP_200_OK
    resp_4 = branch_2.client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_1.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_4.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_moderators_can_approve_revisions_only_for_pages_in_their_branch(
    branch_moderator_factory, root_page
):
    branch_1 = branch_moderator_factory.get(root_page)
    branch_2 = branch_moderator_factory.get(root_page)

    draft_page = exred_factories.ArticlePageFactory(
        parent=branch_2.listing, live=False
    )
    revision = draft_page.save_revision(
        user=branch_2.user, submitted_for_moderation=True
    )

    resp_1 = branch_1.client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk])
    )
    assert resp_1.status_code == status.HTTP_403_FORBIDDEN

    # after publishing a page, user is redirected to the '/admin/' page
    resp_2 = branch_2.client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk]),
        follow=True,
    )
    assert resp_2.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_branch_moderators_cannot_access_pages_from_other_branch(
    branch_moderator_factory, root_page
):
    branch_1 = branch_moderator_factory.get(root_page)
    branch_2 = branch_moderator_factory.get(root_page)

    # Because user_1 doesn't have rights to access page_2
    # it's redirected to the root page to which he has access to (listing_1)
    resp_1 = branch_1.client.get(
        f'/admin/pages/{branch_2.article.pk}/', follow=False
    )
    assert resp_1.status_code == status.HTTP_302_FOUND
    assert resp_1.url == f'/admin/pages/{branch_1.listing.pk}/'

    resp_2 = branch_2.client.get(
        f'/admin/pages/{branch_1.article.pk}/', follow=False
    )
    assert resp_2.status_code == status.HTTP_302_FOUND
    assert resp_2.url == f'/admin/pages/{branch_2.listing.pk}/'


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_create_child_pages(branch_editor_factory, root_page):
    branch = branch_editor_factory.get(root_page)
    data = {
        'article_title': 'test article',
        'article_teaser': 'test article',
        'article_body_text': 'test article',
        'title_en_gb': 'test article',
        'slug': 'test-article',
    }

    resp_1 = branch.client.post(
        reverse(
            'wagtailadmin_pages:add',
            args=[
                branch.article._meta.app_label,
                branch.article._meta.model_name,
                branch.listing.pk],
        ),
        data=data,
    )
    assert (
        resp_1.status_code == status.HTTP_302_FOUND
    ), f'Something went wrong: {resp_1.context["form"].errors}'

    # check if new page is visible in the 'Pages' menu
    new_article_id = int(resp_1.url.split('/')[3])  # format is '/admin/pages/6/edit/'  # NOQA
    resp_2 = branch.client.get(
        f'/admin/api/v2beta/pages/?child_of={branch.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert resp_2.json()['meta']['total_count'] == 2
    assert resp_2.json()['items'][0]['id'] == branch.article.pk
    assert resp_2.json()['items'][1]['id'] == new_article_id


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_cant_create_child_pages_without_mandatory_data(
        branch_editor_factory, root_page
):
    branch = branch_editor_factory.get(root_page)
    mandatory_fields = {
        'article_title',
        'article_teaser',
        'article_body_text',
        'title_en_gb',
        'slug',
    }
    data = {}
    resp = branch.client.post(
        reverse(
            'wagtailadmin_pages:add',
            args=[
                branch.article._meta.app_label,
                branch.article._meta.model_name,
                branch.listing.pk
            ],
        ),
        data=data,
    )
    assert resp.status_code == status.HTTP_200_OK
    assert not (mandatory_fields - set(resp.context['form'].errors.keys()))


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_cant_create_pages_in_branch_they_dont_manage(
        branch_editor_factory, root_page
):
    branch_1 = branch_editor_factory.get(root_page)
    branch_2 = branch_editor_factory.get(root_page)
    data = {
        'article_title': 'test article',
        'article_teaser': 'test article',
        'article_body_text': 'test article',
        'title_en_gb': 'test article',
        'slug': 'test-article',
    }

    resp = branch_1.client.post(
        reverse(
            'wagtailadmin_pages:add',
            args=[
                branch_2.article._meta.app_label,
                branch_2.article._meta.model_name,
                branch_2.listing.pk
            ],
        ),
        data=data,
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_cannot_publish_child_pages(branch_editor_factory, root_page):
    branch = branch_editor_factory.get(root_page)

    draft_page = exred_factories.ArticlePageFactory(
        parent=branch.listing, live=False
    )
    revision = draft_page.save_revision(
        user=branch.user, submitted_for_moderation=True
    )

    resp = branch.client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk])
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_submit_changes_for_moderation(
        branch_editor_factory, root_page
):
    branch = branch_editor_factory.get(root_page)
    data = {
        'article_title': 'new title',
        'article_teaser': 'new teaser',
        'article_body_text': 'new body text',
        'title_en_gb': 'next title',
        'action-submit': 'Submit for moderation',  # this action triggers notification  # NOQA
    }
    resp = branch.client.post(
        reverse('wagtailadmin_pages:edit', args=[branch.article.pk]),
        data=data
    )
    # on success, user should be redirected on parent page listing
    assert resp.status_code == status.HTTP_302_FOUND, resp.context['form'].errors  # NOQA
    assert int(resp.url.split('/')[3]) == branch.listing.pk  # format is /admin/pages/3/  # NOQA


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_view_drafts(branch_editor_factory, root_page):
    branch = branch_editor_factory.get(root_page)
    data = {
        'article_title': 'new title',
        'article_teaser': 'new teaser',
        'article_body_text': 'new body text',
        'title_en_gb': 'next title',
        # omitted 'action-submit' means that pages was save as draft
    }

    # Create a draft and stay on the same admin page
    resp_1 = branch.client.post(
        reverse('wagtailadmin_pages:edit', args=[branch.article.pk]), data=data
    )
    assert resp_1.status_code == status.HTTP_302_FOUND
    assert 'has been updated' in resp_1.context['message']
    assert int(resp_1.url.split('/')[3]) == branch.article.pk  # format is /admin/pages/3/edit/  # NOQA

    # Viewing draft will redirect user to the application site
    resp_2 = branch.client.get(
        reverse('wagtailadmin_pages:view_draft', args=[branch.article.pk])
    )
    assert resp_2.status_code == status.HTTP_302_FOUND
    assert branch.article.slug in resp_2.url


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_list_revisions(branch_editor_factory, root_page):
    branch = branch_editor_factory.get(root_page)

    revision = branch.article.save_revision(
        user=branch.user, submitted_for_moderation=True
    )
    revert_path = f'/admin/pages/{branch.article.pk}/revisions/{revision.pk}/revert/'  # NOQA

    resp = branch.client.get(
        reverse('wagtailadmin_pages:revisions_index', args=[branch.article.pk])
    )
    assert resp.status_code == status.HTTP_200_OK
    assert revert_path in resp.content.decode()


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_compare_changes_between_revisions(
        branch_editor_factory, root_page
):
    branch = branch_editor_factory.get(root_page)

    new_title = 'The title was modified'
    branch.article.title = new_title
    revision = branch.article.save_revision(
        user=branch.user, submitted_for_moderation=True
    )

    # compare current 'live' version of the page with the revision
    resp = branch.client.get(
        reverse(
            'wagtailadmin_pages:revisions_compare',
            args=[branch.article.pk, 'live', revision.id],
        )
    )
    content = resp.content.decode()
    assert resp.status_code == status.HTTP_200_OK
    assert new_title in content
    assert 'There are no differences between these two revisions' \
           not in content

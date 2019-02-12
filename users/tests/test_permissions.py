import pytest
from django.urls import reverse
from rest_framework import status

import export_readiness.tests.factories as exred_factories
from users.tests.factories import BranchEditorFactory, BranchModeratorFactory


@pytest.mark.quirk
@pytest.mark.CMS_837
@pytest.mark.django_db
def test_branch_editors_should_only_see_pages_from_their_branch(
    branch_editor_moderator_factory, distinct_root_pages
):
    root_page_1, root_page_2 = distinct_root_pages
    branch_1 = branch_editor_moderator_factory.get(root_page_1)
    branch_2 = branch_editor_moderator_factory.get(root_page_2)

    # This reproduces Wagtail's admin call to list pages in the 'Pages' menu.
    # Editors should only see app pages that share common root page
    resp_1 = branch_1.editor_client.get(
        f'/admin/api/v2beta/pages/?child_of={root_page_1.pk}&for_explorer=1'
    )
    assert resp_1.status_code == status.HTTP_200_OK
    assert resp_1.json()['meta']['total_count'] == 1
    assert resp_1.json()['items'][0]['id'] == branch_1.listing.pk

    # This reproduces Wagtail's admin call to list pages in the 'Pages' menu.
    # Editors should only see app pages that share common root page
    resp_2 = branch_2.editor_client.get(
        f'/admin/api/v2beta/pages/?child_of={root_page_2.pk}&for_explorer=1'
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert resp_2.json()['meta']['total_count'] == 1
    assert resp_2.json()['items'][0]['id'] == branch_2.listing.pk

    # This reproduces behaviour when Users explore pages using 'Pages' menu
    # User can only see pages that belong to their listing page
    resp_3 = branch_1.editor_client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_1.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_3.status_code == status.HTTP_200_OK
    assert resp_3.json()['meta']['total_count'] == 1
    assert resp_3.json()['items'][0]['id'] == branch_1.article.pk

    # This reproduces behaviour when Users explore pages using 'Pages' menu
    # User can only see pages that belong to their listing page
    resp_5 = branch_2.editor_client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_2.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_5.status_code == status.HTTP_200_OK
    assert resp_5.json()['meta']['total_count'] == 1
    assert resp_5.json()['items'][0]['id'] == branch_2.article.pk

    # Unfortunately on API level Wagtail allows users to list pages that
    # belong to different branch
    resp_5 = branch_1.editor_client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_2.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_5.status_code == status.HTTP_200_OK
    assert resp_5.json()['meta']['total_count'] == 1
    assert resp_5.json()['items'][0]['id'] == branch_2.article.pk

    # Unfortunately on API level Wagtail allows users to list pages that
    # belong to different branch
    resp_6 = branch_2.editor_client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_1.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_6.status_code == status.HTTP_200_OK
    assert resp_6.json()['meta']['total_count'] == 1
    assert resp_6.json()['items'][0]['id'] == branch_1.article.pk


@pytest.mark.quirk
@pytest.mark.CMS_837
@pytest.mark.django_db
def test_branch_moderators_should_only_see_pages_from_their_branch(
        branch_editor_moderator_factory, distinct_root_pages
):
    root_page_1, root_page_2 = distinct_root_pages
    branch_1 = branch_editor_moderator_factory.get(root_page_1)
    branch_2 = branch_editor_moderator_factory.get(root_page_2)

    # This reproduces Wagtail's admin call to list pages in the 'Pages' menu.
    # Editors should only see app pages that share common root page
    resp_1 = branch_1.moderator_client.get(
        f'/admin/api/v2beta/pages/?child_of={root_page_1.pk}&for_explorer=1'
    )
    assert resp_1.status_code == status.HTTP_200_OK
    assert resp_1.json()['meta']['total_count'] == 1
    assert resp_1.json()['items'][0]['id'] == branch_1.listing.pk

    # This reproduces Wagtail's admin call to list pages in the 'Pages' menu.
    # Editors should only see app pages that share common root page
    resp_2 = branch_2.moderator_client.get(
        f'/admin/api/v2beta/pages/?child_of={root_page_2.pk}&for_explorer=1'
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert resp_2.json()['meta']['total_count'] == 1
    assert resp_2.json()['items'][0]['id'] == branch_2.listing.pk

    # This reproduces behaviour when Users explore pages using 'Pages' menu
    # User can only see pages that belong to their listing page
    resp_3 = branch_1.moderator_client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_1.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_3.status_code == status.HTTP_200_OK
    assert resp_3.json()['meta']['total_count'] == 1
    assert resp_3.json()['items'][0]['id'] == branch_1.article.pk

    # This reproduces behaviour when Users explore pages using 'Pages' menu
    # User can only see pages that belong to their listing page
    resp_5 = branch_2.moderator_client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_2.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_5.status_code == status.HTTP_200_OK
    assert resp_5.json()['meta']['total_count'] == 1
    assert resp_5.json()['items'][0]['id'] == branch_2.article.pk

    # Unfortunately on API level Wagtail allows users to list pages that
    # belong to different branch
    resp_5 = branch_1.moderator_client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_2.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_5.status_code == status.HTTP_200_OK
    assert resp_5.json()['meta']['total_count'] == 1
    assert resp_5.json()['items'][0]['id'] == branch_2.article.pk

    # Unfortunately on API level Wagtail allows users to list pages that
    # belong to different branch
    resp_6 = branch_2.moderator_client.get(
        f'/admin/api/v2beta/pages/?child_of={branch_1.listing.pk}&for_explorer=1'  # NOQA
    )
    assert resp_6.status_code == status.HTTP_200_OK
    assert resp_6.json()['meta']['total_count'] == 1
    assert resp_6.json()['items'][0]['id'] == branch_1.article.pk


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
@pytest.mark.CMS_840
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory
    ])
def test_branch_user_can_create_child_pages_in_it(branch_factory, root_page):
    branch = branch_factory.get(root_page)
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
@pytest.mark.CMS_840
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory
    ])
def test_branch_user_cant_create_child_pages_without_mandatory_data(
        branch_factory, root_page
):
    branch = branch_factory.get(root_page)
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
@pytest.mark.CMS_840
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory
    ])
def test_branch_user_cant_create_pages_in_branch_they_dont_manage(
        branch_factory, root_page
):
    branch_1 = branch_factory.get(root_page)
    branch_2 = branch_factory.get(root_page)
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
def test_editors_cannot_unpublish_child_pages(
        branch_editor_factory, root_page
):
    branch = branch_editor_factory.get(root_page)

    resp = branch.client.post(
        reverse('wagtailadmin_pages:unpublish', args=[branch.article.pk])
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.CMS_839
@pytest.mark.CMS_840
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory
    ])
def test_branch_user_can_submit_changes_for_moderation(
        branch_factory, root_page
):
    branch = branch_factory.get(root_page)
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
@pytest.mark.CMS_840
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory
    ])
def test_branch_user_can_view_drafts(branch_factory, root_page):
    branch = branch_factory.get(root_page)
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
@pytest.mark.CMS_840
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory
    ])
def test_branch_users_can_list_revisions(branch_factory, root_page):
    branch = branch_factory.get(root_page)

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
@pytest.mark.CMS_840
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory
    ])
def test_editors_can_compare_changes_between_revisions(
        branch_factory, root_page
):
    branch = branch_factory.get(root_page)

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


@pytest.mark.CMS_840
@pytest.mark.django_db
def test_moderators_can_publish_child_pages(
        branch_moderator_factory, root_page
):
    branch = branch_moderator_factory.get(root_page)

    draft_page = exred_factories.ArticlePageFactory(
        parent=branch.listing, live=False
    )
    revision = draft_page.save_revision(
        user=branch.user, submitted_for_moderation=True
    )

    resp = branch.client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk])
    )
    assert resp.status_code == status.HTTP_302_FOUND
    assert resp.url == '/admin/'


@pytest.mark.CMS_840
@pytest.mark.django_db
def test_moderators_can_unpublish_child_pages(
        branch_moderator_factory, root_page
):
    branch = branch_moderator_factory.get(root_page)

    resp = branch.client.post(
        reverse('wagtailadmin_pages:unpublish', args=[branch.article.pk])
    )
    assert resp.status_code == status.HTTP_302_FOUND
    assert int(resp.url.split('/')[3]) == branch.listing.pk  # format is /admin/pages/4/  # NOQA

    resp_2 = branch.client.get(
        f'/admin/api/v2beta/pages/?child_of={branch.listing.pk}&for_explorer=1'
        # NOQA
    )
    assert resp_2.status_code == status.HTTP_200_OK
    article_status = resp_2.json()['items'][0]['meta']['status']
    assert article_status['status'] == 'draft'
    assert not article_status['live']
    assert article_status['has_unpublished_changes']


@pytest.mark.quirk
@pytest.mark.CMS_840
@pytest.mark.django_db
def test_moderators_can_view_revisions_from_other_branches(
        branch_editor_moderator_factory, root_page
):
    """
    Unfortunately on API level Wagtail allows Moderators to view revisions from
    other branches.
    """
    branch_1 = branch_editor_moderator_factory.get(root_page)
    branch_2 = branch_editor_moderator_factory.get(root_page)

    revision_1 = branch_1.article.save_revision(
        user=branch_1.editor, submitted_for_moderation=True
    )
    revision_2 = branch_2.article.save_revision(
        user=branch_2.editor, submitted_for_moderation=True
    )
    revert_path_1 = f'/admin/pages/{branch_1.article.pk}/revisions/{revision_1.pk}/revert/'  # NOQA
    revert_path_2 = f'/admin/pages/{branch_2.article.pk}/revisions/{revision_2.pk}/revert/'  # NOQA

    resp_1 = branch_1.editor_client.get(
        reverse('wagtailadmin_pages:revisions_index',
                args=[branch_1.article.pk])
    )
    assert resp_1.status_code == status.HTTP_200_OK
    content_1 = resp_1.content.decode()
    assert revert_path_1 in content_1
    assert revert_path_2 not in content_1

    resp_2 = branch_1.editor_client.get(
        reverse('wagtailadmin_pages:revisions_index',
                args=[branch_2.article.pk])
    )
    assert resp_2.status_code == status.HTTP_200_OK
    content_2 = resp_2.content.decode()
    assert revert_path_1 not in content_2
    assert revert_path_2 in content_2

    resp_3 = branch_2.editor_client.get(
        reverse('wagtailadmin_pages:revisions_index',
                args=[branch_1.article.pk])
    )
    assert resp_3.status_code == status.HTTP_200_OK
    content_3 = resp_3.content.decode()
    assert revert_path_1 in content_3
    assert revert_path_2 not in content_3

    resp_4 = branch_2.editor_client.get(
        reverse('wagtailadmin_pages:revisions_index',
                args=[branch_2.article.pk])
    )
    assert resp_4.status_code == status.HTTP_200_OK
    content_4 = resp_4.content.decode()
    assert revert_path_1 not in content_4
    assert revert_path_2 in content_4


@pytest.mark.CMS_840
@pytest.mark.django_db
def test_moderators_can_reject_revision(
        branch_editor_moderator_factory, root_page
):
    branch = branch_editor_moderator_factory.get(root_page)

    new_title = 'The title was modified'
    branch.article.title = new_title
    revision = branch.article.save_revision(
        user=branch.editor, submitted_for_moderation=True
    )

    # Reject request for moderation
    resp_1 = branch.moderator_client.post(
        reverse('wagtailadmin_pages:reject_moderation', args=[revision.pk])
    )
    assert resp_1.status_code == status.HTTP_302_FOUND
    assert resp_1.url == '/admin/'

    # Verify if rejection is visible
    resp_2 = branch.moderator_client.get(
        reverse('wagtailadmin_pages:revisions_index', args=[branch.article.pk])
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert 'rejected for publication' in resp_2.content.decode()


@pytest.mark.CMS_840
@pytest.mark.django_db
def test_moderators_cannot_reject_revision_from_other_branch(
        branch_editor_moderator_factory, root_page
):
    branch_1 = branch_editor_moderator_factory.get(root_page)
    branch_2 = branch_editor_moderator_factory.get(root_page)

    new_title = 'The title was modified'
    branch_1.article.title = new_title
    revision = branch_1.article.save_revision(
        user=branch_1.editor, submitted_for_moderation=True
    )

    # Reject request for moderation
    resp = branch_2.moderator_client.post(
        reverse('wagtailadmin_pages:reject_moderation', args=[revision.pk])
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN

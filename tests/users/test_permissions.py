import pytest
from django.urls import reverse
from rest_framework import status

from tests.export_readiness.factories import ArticlePageFactory
from tests.users.factories import (
    AdminFactory,
    BranchEditorFactory,
    BranchModeratorFactory,
    two_branches_with_users,
)


@pytest.mark.CMS_837
@pytest.mark.django_db
def test_branch_editors_should_only_see_pages_from_their_branch(root_page, international_root_page):
    """
    This reproduces Wagtail's admin call to list pages in the 'Pages' menu.
    Editors should only see app pages that share common root page
    """
    env = two_branches_with_users(root_page, international_root_page)

    resp_1 = env.editor_1_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.landing_1.pk}&for_explorer=1'
    )
    assert resp_1.status_code == status.HTTP_200_OK
    assert resp_1.json()['meta']['total_count'] == 1
    assert resp_1.json()['items'][0]['id'] == env.listing_1.pk

    resp_2 = env.editor_2_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.landing_2.pk}&for_explorer=1'
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert resp_2.json()['meta']['total_count'] == 1
    assert resp_2.json()['items'][0]['id'] == env.listing_2.pk


@pytest.mark.quirk
@pytest.mark.CMS_837
@pytest.mark.django_db
def test_branch_editors_cannot_access_pages_not_from_their_branch(root_page, international_root_page):
    """
    This reproduces situation when an editor would try to access page that
    doesn't belong to they branch by simply changing page ID in the URL
    """
    env = two_branches_with_users(root_page, international_root_page)

    resp_1 = env.editor_1_client.get(f'/admin/pages/{env.home_2.pk}/edit/')
    assert resp_1.status_code == status.HTTP_403_FORBIDDEN

    resp_2 = env.editor_2_client.get(f'/admin/pages/{env.home_1.pk}/edit/')
    assert resp_2.status_code == status.HTTP_403_FORBIDDEN

    resp_3 = env.editor_1_client.get(f'/admin/pages/{env.home_2.pk}/')
    assert resp_3.status_code == status.HTTP_302_FOUND
    assert resp_3.url == f'/admin/pages/{env.home_1.pk}/'

    resp_4 = env.editor_2_client.get(f'/admin/pages/{env.home_1.pk}/')
    assert resp_4.status_code == status.HTTP_302_FOUND
    assert resp_4.url == f'/admin/pages/{env.home_2.pk}/'

    # Unfortunately on API level Wagtail allows users to list pages that
    # belong to different branch
    resp_6 = env.editor_1_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.landing_2.pk}&for_explorer=1'  # NOQA
    )
    assert resp_6.status_code == status.HTTP_200_OK
    assert resp_6.json()['meta']['total_count'] == 1
    assert resp_6.json()['items'][0]['id'] == env.listing_2.pk


@pytest.mark.CMS_837
@pytest.mark.django_db
def test_branch_moderators_should_only_see_pages_from_their_branch(root_page, international_root_page):
    """
    This reproduces Wagtail's admin call to list pages in the 'Pages' menu.
    Moderators should only see app pages that share common root page
    """
    env = two_branches_with_users(root_page, international_root_page)

    resp_1 = env.moderator_1_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.landing_1.pk}&for_explorer=1'
    )
    assert resp_1.status_code == status.HTTP_200_OK
    assert resp_1.json()['meta']['total_count'] == 1
    assert resp_1.json()['items'][0]['id'] == env.listing_1.pk

    resp_2 = env.moderator_2_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.landing_2.pk}&for_explorer=1'
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert resp_2.json()['meta']['total_count'] == 1
    assert resp_2.json()['items'][0]['id'] == env.listing_2.pk


@pytest.mark.quirk
@pytest.mark.CMS_837
@pytest.mark.django_db
def test_moderators_cannot_access_pages_not_from_their_branch(root_page, international_root_page):
    """
    This reproduces situation when a moderator would try to access page that
    doesn't belong to they branch by simply changing page ID in the URL
    """
    env = two_branches_with_users(root_page, international_root_page)

    resp_1 = env.moderator_1_client.get(
        f'/admin/pages/{env.home_2.pk}/edit/'
    )
    assert resp_1.status_code == status.HTTP_403_FORBIDDEN

    resp_2 = env.moderator_2_client.get(
        f'/admin/pages/{env.home_1.pk}/edit/'
    )
    assert resp_2.status_code == status.HTTP_403_FORBIDDEN

    resp_3 = env.moderator_1_client.get(f'/admin/pages/{env.home_2.pk}/')
    assert resp_3.status_code == status.HTTP_302_FOUND
    assert resp_3.url == f'/admin/pages/{env.home_1.pk}/'

    resp_4 = env.moderator_2_client.get(f'/admin/pages/{env.home_1.pk}/')
    assert resp_4.status_code == status.HTTP_302_FOUND
    assert resp_4.url == f'/admin/pages/{env.home_2.pk}/'

    # Unfortunately on API level Wagtail allows users to list pages that
    # belong to different branch
    resp_6 = env.moderator_1_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.landing_2.pk}&for_explorer=1'
    )
    assert resp_6.status_code == status.HTTP_200_OK
    assert resp_6.json()['meta']['total_count'] == 1
    assert resp_6.json()['items'][0]['id'] == env.listing_2.pk


@pytest.mark.django_db
def test_moderators_can_approve_revisions_only_for_pages_in_their_branch(
    root_page, international_root_page
):
    env = two_branches_with_users(root_page, international_root_page)

    new_title = 'The title was modified'
    env.article_2.title = new_title
    revision = env.article_2.save_revision(
        user=env.editor_2, submitted_for_moderation=True
    )

    resp_1 = env.moderator_1_client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk])
    )
    assert resp_1.status_code == status.HTTP_403_FORBIDDEN

    # after publishing a page, user is redirected to the '/admin/' page
    resp_2 = env.moderator_2_client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk]),
        follow=True,
    )
    assert resp_2.status_code == status.HTTP_200_OK


@pytest.mark.CMS_839
@pytest.mark.CMS_840
@pytest.mark.CMS_841
@pytest.mark.django_db
@pytest.mark.parametrize(
    'branch_factory', [
        BranchEditorFactory,
        BranchModeratorFactory,
        AdminFactory,
    ])
def test_branch_user_can_create_child_pages_in_it(branch_factory, root_page):
    branch = branch_factory.get(root_page)
    data = {
        'type_of_article': 'Blog',
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
@pytest.mark.CMS_841
@pytest.mark.django_db
@pytest.mark.parametrize(
    'branch_factory', [
        BranchEditorFactory,
        BranchModeratorFactory,
        AdminFactory,
    ])
def test_branch_user_cant_create_child_pages_without_mandatory_data(
        branch_factory, root_page
):
    branch = branch_factory.get(root_page)
    mandatory_fields = {
        'type_of_article',
        'article_title',
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
    'branch_factory', [
        BranchEditorFactory,
        BranchModeratorFactory,
    ])
def test_branch_user_cant_create_pages_in_branch_they_dont_manage(
        branch_factory, root_page
):
    branch_1 = branch_factory.get(root_page)
    branch_2 = branch_factory.get(root_page)
    data = {
        'type_of_article': 'Blog',
        'article_title': 'test article',
        'article_teaser': 'test article',
        'article_body_text': 'test article',
        'title_en_gb': 'test article',
        'slug': 'test-article',
        'action-publish': 'action-publish',
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


@pytest.mark.CMS_841
@pytest.mark.django_db
def test_admins_can_create_pages_in_any_branch(root_page, international_root_page):
    env = two_branches_with_users(root_page, international_root_page)

    # Add exread Article page
    data_1 = {
        'type_of_article': 'Blog',
        'article_title': 'test article',
        'article_teaser': 'test article',
        'article_body_text': 'test article',
        'title_en_gb': 'test article',
        'slug': 'test-article',
        'action-publish': 'action-publish',
    }

    resp_1 = env.admin_client.post(
        reverse(
            'wagtailadmin_pages:add',
            args=[
                env.article_1._meta.app_label,
                env.article_1._meta.model_name,
                env.listing_1.pk
            ],
        ),
        data=data_1,
    )
    assert resp_1.status_code == status.HTTP_302_FOUND
    assert resp_1.url.startswith('/admin/pages/')  # format is /admin/pages/3/

    # Add international Article page
    data_2 = {
        'type_of_article': 'Blog',
        'article_title_en_gb': 'test article',
        'article_body_text_en_gb': 'test article',
        'title_en_gb': 'test article',
        'slug': 'test-article',
        'action-publish': 'action-publish',
    }
    resp_2 = env.admin_client.post(
        reverse(
            'wagtailadmin_pages:add',
            args=[
                env.article_2._meta.app_label,
                env.article_2._meta.model_name,
                env.listing_2.pk
            ],
        ),
        data=data_2,
    )
    assert resp_2.status_code == status.HTTP_302_FOUND
    assert resp_2.url.startswith('/admin/pages/')  # format is /admin/pages/3/


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_cannot_publish_child_pages(root_page, international_root_page):
    env = two_branches_with_users(root_page, international_root_page)

    draft_page = ArticlePageFactory(
        parent=env.landing_1, live=False
    )
    revision = draft_page.save_revision(
        user=env.editor_1, submitted_for_moderation=True
    )

    resp = env.editor_1_client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk])
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_cannot_unpublish_child_pages(root_page, international_root_page):
    env = two_branches_with_users(root_page, international_root_page)

    resp = env.editor_1_client.post(
        reverse('wagtailadmin_pages:unpublish', args=[env.article_1.pk])
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.CMS_839
@pytest.mark.CMS_840
@pytest.mark.CMS_841
@pytest.mark.django_db
@pytest.mark.parametrize(
    'branch_factory', [
        BranchEditorFactory,
        BranchModeratorFactory,
        AdminFactory,
    ])
def test_branch_user_can_submit_changes_for_moderation(
        branch_factory, root_page
):
    branch = branch_factory.get(root_page)
    data = {
        'type_of_article': 'Blog',
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
@pytest.mark.CMS_841
@pytest.mark.django_db
@pytest.mark.parametrize(
    'branch_factory', [
        BranchEditorFactory,
        BranchModeratorFactory,
        AdminFactory,
    ])
def test_branch_user_can_view_drafts(branch_factory, root_page):
    branch = branch_factory.get(root_page)
    data = {
        'type_of_article': 'Blog',
        'article_title': 'new title',
        'article_teaser': 'new teaser',
        'article_body_text': 'new body text',
        'title_en_gb': 'next title',
        # omitted 'action-submit' means that pages was saved as draft
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
@pytest.mark.CMS_841
@pytest.mark.django_db
@pytest.mark.parametrize(
    'branch_factory', [
        BranchEditorFactory,
        BranchModeratorFactory,
        AdminFactory,
    ])
def test_branch_user_can_list_revisions(branch_factory, root_page):
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
@pytest.mark.CMS_841
@pytest.mark.django_db
@pytest.mark.parametrize(
    'branch_factory', [
        BranchEditorFactory,
        BranchModeratorFactory,
        AdminFactory,
    ])
def test_branch_user_can_compare_changes_between_revisions(
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
@pytest.mark.CMS_841
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchModeratorFactory,
        AdminFactory,
    ])
def test_moderators_and_admins_can_publish_child_pages(
        branch_factory, root_page
):
    branch = branch_factory.get(root_page)

    draft_page = ArticlePageFactory(parent=branch.listing, live=False)
    revision = draft_page.save_revision(
        user=branch.user, submitted_for_moderation=True,
    )

    resp = branch.client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk])
    )
    assert resp.status_code == status.HTTP_302_FOUND
    assert resp.url == '/admin/'


@pytest.mark.CMS_840
@pytest.mark.CMS_841
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchModeratorFactory,
        AdminFactory,
    ])
def test_moderators_and_admins_can_unpublish_child_pages(
        branch_factory, root_page
):
    branch = branch_factory.get(root_page)

    resp = branch.client.post(
        reverse('wagtailadmin_pages:unpublish', args=[branch.article.pk])
    )
    assert resp.status_code == status.HTTP_302_FOUND
    assert int(resp.url.split('/')[3]) == branch.listing.pk  # format is /admin/pages/4/  # NOQA

    resp_2 = branch.client.get(
        f'/admin/api/v2beta/pages/?child_of={branch.listing.pk}&for_explorer=1'
    )
    assert resp_2.status_code == status.HTTP_200_OK
    article_status = resp_2.json()['items'][0]['meta']['status']
    assert article_status['status'] == 'draft'
    assert not article_status['live']
    assert article_status['has_unpublished_changes']


@pytest.mark.quirk
@pytest.mark.CMS_840
@pytest.mark.CMS_841
@pytest.mark.django_db
def test_moderators_and_admins_can_view_revisions_from_other_branches(
        root_page, international_root_page
):
    """
    Unfortunately on API level Wagtail allows Moderators to view revisions from
    other branches.
    """
    env = two_branches_with_users(root_page, international_root_page)

    revision_1 = env.article_1.save_revision(
        user=env.editor_1, submitted_for_moderation=True
    )
    revision_2 = env.article_2.save_revision(
        user=env.editor_2, submitted_for_moderation=True
    )
    revert_path_1 = f'/admin/pages/{env.article_1.pk}/revisions/{revision_1.pk}/revert/'  # NOQA
    revert_path_2 = f'/admin/pages/{env.article_2.pk}/revisions/{revision_2.pk}/revert/'  # NOQA

    resp_1 = env.moderator_1_client.get(
        reverse('wagtailadmin_pages:revisions_index',
                args=[env.article_1.pk])
    )
    assert resp_1.status_code == status.HTTP_200_OK
    content_1 = resp_1.content.decode()
    assert revert_path_1 in content_1
    assert revert_path_2 not in content_1

    resp_2 = env.moderator_1_client.get(
        reverse('wagtailadmin_pages:revisions_index',
                args=[env.article_2.pk])
    )
    assert resp_2.status_code == status.HTTP_200_OK
    content_2 = resp_2.content.decode()
    assert revert_path_1 not in content_2
    assert revert_path_2 in content_2

    resp_3 = env.moderator_2_client.get(
        reverse('wagtailadmin_pages:revisions_index',
                args=[env.article_1.pk])
    )
    assert resp_3.status_code == status.HTTP_200_OK
    content_3 = resp_3.content.decode()
    assert revert_path_1 in content_3
    assert revert_path_2 not in content_3

    resp_4 = env.moderator_2_client.get(
        reverse('wagtailadmin_pages:revisions_index',
                args=[env.article_2.pk])
    )
    assert resp_4.status_code == status.HTTP_200_OK
    content_4 = resp_4.content.decode()
    assert revert_path_1 not in content_4
    assert revert_path_2 in content_4


@pytest.mark.CMS_840
@pytest.mark.CMS_841
@pytest.mark.django_db
def test_moderators_can_reject_revision(root_page, international_root_page):
    env = two_branches_with_users(root_page, international_root_page)

    new_title = 'The title was modified'
    env.article_1.title = new_title
    revision = env.article_1.save_revision(
        user=env.editor_1, submitted_for_moderation=True
    )

    # Reject request for moderation
    resp_1 = env.moderator_1_client.post(
        reverse('wagtailadmin_pages:reject_moderation', args=[revision.pk])
    )
    assert resp_1.status_code == status.HTTP_302_FOUND
    assert resp_1.url == '/admin/'

    # Verify if rejection is visible
    resp_2 = env.moderator_1_client.get(
        reverse('wagtailadmin_pages:revisions_index', args=[env.article_1.pk])
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert 'rejected for publication' in resp_2.content.decode()


@pytest.mark.CMS_841
@pytest.mark.django_db
def test_admins_can_reject_revision(root_page, international_root_page):
    env = two_branches_with_users(root_page, international_root_page)

    new_title = 'The title was modified'
    env.article_1.title = new_title
    revision = env.article_1.save_revision(
        user=env.editor_1, submitted_for_moderation=True
    )

    # Reject request for moderation
    resp_1 = env.admin_client.post(
        reverse('wagtailadmin_pages:reject_moderation', args=[revision.pk])
    )
    assert resp_1.status_code == status.HTTP_302_FOUND
    assert resp_1.url == '/admin/'

    # Verify if rejection is visible
    resp_2 = env.admin_client.get(
        reverse('wagtailadmin_pages:revisions_index', args=[env.article_1.pk])
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert 'rejected for publication' in resp_2.content.decode()


@pytest.mark.CMS_840
@pytest.mark.django_db
def test_moderators_cannot_reject_revision_from_other_branch(root_page, international_root_page):
    env = two_branches_with_users(root_page, international_root_page)

    new_title = 'The title was modified'
    env.article_1.title = new_title
    revision = env.article_1.save_revision(
        user=env.editor_1, submitted_for_moderation=True
    )

    # Reject request for moderation
    resp = env.moderator_2_client.post(
        reverse('wagtailadmin_pages:reject_moderation', args=[revision.pk])
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.CMS_836
@pytest.mark.django_db
def test_admins_should_be_able_to_access_all_pages_in_any_branch(root_page, international_root_page):
    env = two_branches_with_users(root_page, international_root_page)

    resp_1 = env.admin_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.landing_1.pk}&for_explorer=1'
    )
    assert resp_1.status_code == status.HTTP_200_OK

    resp_2 = env.admin_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.landing_2.pk}&for_explorer=1'
    )
    assert resp_2.status_code == status.HTTP_200_OK

    resp_3 = env.admin_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.article_1.pk}&for_explorer=1'
    )
    assert resp_3.status_code == status.HTTP_200_OK

    resp_4 = env.admin_client.get(
        f'/admin/api/v2beta/pages/?child_of={env.article_2.pk}&for_explorer=1'
    )
    assert resp_4.status_code == status.HTTP_200_OK


@pytest.mark.quirk
@pytest.mark.CMS_836
@pytest.mark.django_db
def test_admins_should_be_able_to_reject_revision_from_any_branch(root_page, international_root_page):
    """
    Somehow Wagtail doesn't show to the editor that revision was rejected
    and thus we have to use Admin client to check that (in last assertion)
    """
    env = two_branches_with_users(root_page, international_root_page)

    # At this point there should be no revisions
    resp_1 = env.editor_1_client.get(
        reverse(
            'wagtailadmin_pages:revisions_index',
            args=[env.article_1.pk]
        )
    )
    assert 'No revision of this page exist' in resp_1.content.decode()

    # Make a change and save revision
    new_title = 'The title was modified'
    env.article_1.title = new_title
    revision = env.article_1.save_revision(
        user=env.editor_1, submitted_for_moderation=True
    )

    # Check if revision is visible
    resp_2 = env.editor_1_client.get(
        reverse(
            'wagtailadmin_pages:revisions_index',
            args=[env.article_1.pk]
        )
    )
    assert new_title in resp_2.content.decode()
    revert_url = f'/admin/pages/{env.article_1.pk}/revisions/{revision.pk}/revert/'  # NOQA
    assert revert_url in resp_2.content.decode()

    # Reject request for moderation
    resp_3 = env.admin_client.post(
        reverse('wagtailadmin_pages:reject_moderation', args=[revision.pk])
    )
    assert resp_3.status_code == status.HTTP_302_FOUND
    assert resp_3.url == '/admin/'

    # Verify if rejection is visible
    resp_4 = env.admin_client.get(
        reverse(
            'wagtailadmin_pages:revisions_index',
            args=[env.article_1.pk]
        )
    )
    assert resp_4.status_code == status.HTTP_200_OK
    assert 'rejected for publication' in resp_4.content.decode()


@pytest.mark.CMS_841
@pytest.mark.django_db
def test_admins_should_have_permissions_to_manage_users(root_page):
    """Admins should have all required permissions to manage users."""
    admin = AdminFactory.get(root_page)
    permissions = {
        'auth.add_group',
        'auth.add_permission',
        'auth.add_user',
        'auth.change_group',
        'auth.change_permission',
        'auth.change_user',
        'auth.delete_group',
        'auth.delete_permission',
        'auth.delete_user',
        'wagtailusers.add_userprofile',
        'wagtailusers.change_userprofile',
        'wagtailusers.delete_userprofile',
    }
    assert not (permissions - admin.user.get_all_permissions())


@pytest.mark.CMS_838
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory,
    ])
def test_non_admin_user_should_not_have_permissions_to_manage_user_accounts(
        branch_factory, root_page
):
    """Non-admin users should not have permissions to manage user accounts"""
    branch = branch_factory.get(root_page)
    permissions = {
        'auth.add_group',
        'auth.add_permission',
        'auth.add_user',
        'auth.change_group',
        'auth.change_permission',
        'auth.change_user',
        'auth.delete_group',
        'auth.delete_permission',
        'auth.delete_user',
        'wagtailusers.add_userprofile',
        'wagtailusers.change_userprofile',
        'wagtailusers.delete_userprofile',
    }
    assert (permissions - branch.user.get_all_permissions()) == permissions


@pytest.mark.CMS_838
@pytest.mark.django_db
@pytest.mark.parametrize(
    "branch_factory", [
        BranchEditorFactory,
        BranchModeratorFactory,
    ])
def test_non_admin_user_should_not_be_able_to_access_manage_users_page(
        branch_factory, root_page
):
    """Non-admin users can't access '/admin/users/' page"""
    branch = branch_factory.get(root_page)
    resp = branch.client.get(reverse('wagtailusers_users:index'), follow=True)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.context['url'] == '/admin/pages/'
    content = resp.content.decode()
    assert 'Sorry, you do not have permission to access this area.' in content


@pytest.mark.CMS_838
@pytest.mark.django_db
def test_admin_user_should_be_able_to_access_manage_users_page(root_page):
    """Admins can access '/admin/users/' page"""
    admin = AdminFactory.get(root_page)
    resp = admin.client.get(reverse('wagtailusers_users:index'))
    assert resp.status_code == status.HTTP_200_OK

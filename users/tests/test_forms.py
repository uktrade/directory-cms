import pytest
from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status

import export_readiness.tests.factories as exred_factories
from .factories import UserFactory, GroupPagePermissionFactory
from export_readiness.tests.factories import ArticleListingPageFactory
from users.forms import UserCreationForm


@pytest.mark.django_db
def test_super_user_can_see_all_the_groups():
    user = UserFactory(is_superuser=True, is_staff=True)
    form = UserCreationForm(user=user)
    all_groups_count = Group.objects.all().count()
    assert form.fields['groups'].queryset.count() == all_groups_count


@pytest.mark.django_db
def test_user_can_see_same_entry_point_groups(root_page):
    page = ArticleListingPageFactory(parent=root_page)
    group_page_one = GroupPagePermissionFactory(
        page=page
    )
    group_page_two = GroupPagePermissionFactory(
        page=page
    )
    user = UserFactory(
        is_superuser=False,
        is_staff=False,
        groups=[group_page_one.group]
    )
    form = UserCreationForm(user=user)
    assert list(
        form.fields['groups'].queryset.values_list('pk', flat=True)
    ) == [group_page_one.group.pk, group_page_two.group.pk]


@pytest.mark.django_db
def test_normal_user_with_no_group_assigned_sees_no_groups():
    user = UserFactory(is_superuser=False, is_staff=False)
    form = UserCreationForm(user=user)
    assert form.fields['groups'].queryset.count() == 0


@pytest.mark.CMS_837
@pytest.mark.django_db
def test_branch_moderators_should_see_pages_only_from_their_branch(branch_moderator_factory):
    listing_1, article_1, _, _, client_1 = branch_moderator_factory.get()
    listing_2, _, _, _, client_2 = branch_moderator_factory.get()

    # This reproduces Wagtail's Admin call to list pages in the "Pages" menu
    # User can only see pages that are child of requested page to which he has access to
    resp_1 = client_1.get(f'/admin/api/v2beta/pages/?child_of={listing_1.pk}&for_explorer=1')
    assert resp_1.status_code == status.HTTP_200_OK
    assert resp_1.json()['meta']['total_count'] == 1
    assert resp_1.json()['items'][0]['id'] == article_1.pk

    # This reproduces situation when User navigates down the "Pages" menu
    # User shouldn't see any child pages of an article as it doesn't have any
    resp_2 = client_1.get(f'/admin/api/v2beta/pages/?child_of={article_1.pk}&for_explorer=1')
    assert resp_2.status_code == status.HTTP_200_OK
    assert resp_2.json()['meta']['total_count'] == 0
    assert not resp_2.json()['items']

    # On API level Wagtail allows users to list pages that belong to different group!
    resp_3 = client_1.get(f'/admin/api/v2beta/pages/?child_of={listing_2.pk}&for_explorer=1')
    assert resp_3.status_code == status.HTTP_200_OK
    resp_4 = client_2.get(f'/admin/api/v2beta/pages/?child_of={listing_1.pk}&for_explorer=1')
    assert resp_4.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_moderators_can_approve_revisions_only_for_pages_in_their_branch(branch_moderator_factory):
    _, _, _, _, client_1 = branch_moderator_factory.get()
    listing_2, _, _, user_2, client_2 = branch_moderator_factory.get()

    draft_page = exred_factories.ArticlePageFactory(parent=listing_2, live=False)
    revision = draft_page.save_revision(user=user_2, submitted_for_moderation=True)

    resp_1 = client_1.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk])
    )
    assert resp_1.status_code == status.HTTP_403_FORBIDDEN

    # after publishing a page, user is redirected to the "/admin/" page
    resp_2 = client_2.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk]),
        follow=True,
    )
    assert resp_2.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_branch_moderators_cannot_access_pages_from_other_branch(branch_moderator_factory):
    listing_1, article_1, _, _, client_1 = branch_moderator_factory.get()
    listing_2, article_2, _, _, client_2 = branch_moderator_factory.get()

    # Because user_1 doesn't have rights to access page_2
    # it's redirected to the root page to which he has access to (listing_1)
    resp_1 = client_1.get(f'/admin/pages/{article_2.pk}/', follow=False)
    assert resp_1.status_code == status.HTTP_302_FOUND
    assert resp_1.url == f'/admin/pages/{listing_1.pk}/'

    resp_2 = client_2.get(f'/admin/pages/{article_1.pk}/', follow=False)
    assert resp_2.status_code == status.HTTP_302_FOUND
    assert resp_2.url == f'/admin/pages/{listing_2.pk}/'


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_create_child_pages(branch_editor_factory):
    listing, article, _, _, client = branch_editor_factory.get()
    data = {
        "article_title": "test article",
        "article_teaser": "test article",
        "article_body_text": "test article",
        "title_en_gb": "test article",
        "slug": "test-article",
    }

    resp_1 = client.post(
        reverse('wagtailadmin_pages:add',
                args=(
                    article._meta.app_label,
                    article._meta.model_name,
                    listing.pk,
                )),
        data=data,
    )
    assert resp_1.status_code == status.HTTP_302_FOUND, (
        f"Something went wrong: {resp_1.context['form'].errors}"
    )

    # check if new page is visible in the "Pages" menu
    new_article_id = int(resp_1.url.split('/')[3])  # format is "/admin/pages/6/edit/"
    resp_2 = client.get(
        f'/admin/api/v2beta/pages/?child_of={listing.pk}&for_explorer=1'
    )
    assert resp_2.status_code == status.HTTP_200_OK
    assert resp_2.json()['meta']['total_count'] == 2
    assert resp_2.json()['items'][0]['id'] == article.pk
    assert resp_2.json()['items'][1]['id'] == new_article_id


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_cant_create_child_pages_without_mandatory_data(branch_editor_factory):
    listing, article, _, _, client = branch_editor_factory.get()
    mandatory_fields = {
        "article_title", "article_teaser", "article_body_text", "title_en_gb", "slug"
    }
    data = {}
    resp = client.post(
        reverse('wagtailadmin_pages:add',
                args=(
                    article._meta.app_label,
                    article._meta.model_name,
                    listing.pk,
                )),
        data=data,
    )
    assert resp.status_code == status.HTTP_200_OK
    assert not (mandatory_fields - set(resp.context['form'].errors.keys()))


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_cant_create_pages_in_branch_they_dont_manage(branch_editor_factory):
    _, _, _, _, client_1 = branch_editor_factory.get()
    listing_2, article_2, _, _, _ = branch_editor_factory.get()
    data = {
        "article_title": "test article",
        "article_teaser": "test article",
        "article_body_text": "test article",
        "title_en_gb": "test article",
        "slug": "test-article",
    }

    resp = client_1.post(
        reverse('wagtailadmin_pages:add',
                args=(
                    article_2._meta.app_label,
                    article_2._meta.model_name,
                    listing_2.pk,
                )),
        data=data,
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_cannot_publish_child_pages(branch_editor_factory):
    listing, _, _, user, client = branch_editor_factory.get()

    draft_page = exred_factories.ArticlePageFactory(parent=listing, live=False)
    revision = draft_page.save_revision(user=user, submitted_for_moderation=True)

    resp = client.post(
        reverse('wagtailadmin_pages:approve_moderation', args=[revision.pk])
    )
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_submit_changes_for_moderation(branch_editor_factory):
    listing, article, _, _, client = branch_editor_factory.get()
    data = {
        "article_title": "new title",
        "article_teaser": "new teaser",
        "article_body_text": "new body text",
        "title_en_gb": "next title",
        "action-submit": "Submit for moderation",  # this action triggers notification
    }
    resp = client.post(
        reverse('wagtailadmin_pages:edit', args=[article.pk]),
        data=data,
    )
    # on success, user should be redirected on parent page listing
    assert resp.status_code == status.HTTP_302_FOUND, resp.context['form'].errors
    assert int(resp.url.split('/')[3]) == listing.pk  # format is /admin/pages/3/


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_view_drafts(branch_editor_factory):
    _, article, _, _, client = branch_editor_factory.get()
    data = {
        "article_title": "new title",
        "article_teaser": "new teaser",
        "article_body_text": "new body text",
        "title_en_gb": "next title",
        # omitted "action-submit" means that pages was save as draft
    }

    # Create a draft and stay on the same admin page
    resp_1 = client.post(
        reverse('wagtailadmin_pages:edit', args=[article.pk]),
        data=data,
    )
    assert resp_1.status_code == status.HTTP_302_FOUND
    assert "has been updated" in resp_1.context['message']
    assert int(resp_1.url.split('/')[3]) == article.pk  # format is /admin/pages/3/edit/

    # Viewing draft will redirect user to the application site
    resp_2 = client.get(
        reverse('wagtailadmin_pages:view_draft', args=[article.pk])
    )
    assert resp_2.status_code == status.HTTP_302_FOUND
    assert article.slug in resp_2.url


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_list_revisions(branch_editor_factory):
    _, article, _, user, client = branch_editor_factory.get()

    revision = article.save_revision(user=user, submitted_for_moderation=True)
    revert_path = f'/admin/pages/{article.pk}/revisions/{revision.pk}/revert/'

    resp = client.get(
        reverse('wagtailadmin_pages:revisions_index', args=[article.pk])
    )
    assert resp.status_code == status.HTTP_200_OK
    assert revert_path in resp.content.decode()


@pytest.mark.CMS_839
@pytest.mark.django_db
def test_editors_can_compare_changes_between_revisions(branch_editor_factory):
    _, article, _, user, client = branch_editor_factory.get()

    new_title = 'The title was modified'
    article.title = new_title
    revision = article.save_revision(user=user, submitted_for_moderation=True)

    # compare current 'live' version of the page with the revision
    resp = client.get(
        reverse(
            'wagtailadmin_pages:revisions_compare',
            args=[article.pk, 'live', revision.id]
        )
    )
    content = resp.content.decode()
    assert resp.status_code == status.HTTP_200_OK
    assert new_title in content
    assert "There are no differences between these two revisions" not in content

from collections import namedtuple

import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import Client
from wagtail.core.models import GroupPagePermission, PAGE_PERMISSION_TYPES

from export_readiness.tests.factories import (
    ArticleListingPageFactory,
    ArticlePageFactory,
)

User = get_user_model()
Branch = namedtuple(
    'Branch', ['listing', 'article', 'group', 'user', 'client']
)
BranchEditorAndModerator = namedtuple(
    'BranchEditorAndModerator', [
        'listing',
        'article',
        'editors',
        'editor',
        'editor_client',
        'moderators',
        'moderator',
        'moderator_client'
    ]
)


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n: "group %s" % n)


class GroupPagePermissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupPagePermission

    group = factory.SubFactory(GroupFactory)
    page = factory.SubFactory(ArticleListingPageFactory)
    permission_type = 'add'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user %s" % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_superuser = False
    is_staff = False

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)


def create_listing_with_article_and_group_with_user_and_client(
        root_page,
        *,
        permissions=[],
        password='test',
        is_superuser=False,
        is_staff=False
):
    """Returns a listing page with a child page, user group, user & client.

    For Wagtail permission model check:
    http://docs.wagtail.io/en/v2.0/topics/permissions.html#page-permissions
    """
    # ensure that only permissions supported by Wagtail are used
    available_permissions = [p for p, _, _ in PAGE_PERMISSION_TYPES]
    assert not (set(permissions) - set(available_permissions))

    listing_page = ArticleListingPageFactory(parent=root_page)
    article_page = ArticlePageFactory(parent=listing_page)

    group = GroupFactory()
    group.permissions.add(Permission.objects.get(codename='access_admin'))

    for permission in permissions:
        GroupPagePermissionFactory(
            page=listing_page, group=group, permission_type=permission)

    user = UserFactory(
        is_superuser=is_superuser, is_staff=is_staff, groups=[group]
    )
    user_password = password or 'test'
    user.set_password(user_password)
    user.save()

    client = Client()
    client.login(username=user.username, password=user_password)

    return Branch(listing_page, article_page, group, user, client)


def create_listing_with_article_and_group_with_editor_and_moderator(
        root_page,
        *,
        editor_permissions=['add', 'edit'],
        editor_password=None,
        editor_is_superuser=False,
        editor_is_staff=False,
        moderator_permissions=['add', 'edit', 'publish'],
        moderator_password=None,
        moderator_is_superuser=False,
        moderator_is_staff=False
):
    """Returns a listing page with a child page, user group, users & clients.

    For Wagtail permission model check:
    http://docs.wagtail.io/en/v2.0/topics/permissions.html#page-permissions
    """
    # ensure that only permissions supported by Wagtail are used
    available_permissions = [p for p, _, _ in PAGE_PERMISSION_TYPES]
    assert not (set(editor_permissions) - set(available_permissions))
    assert not (set(moderator_permissions) - set(available_permissions))

    listing_page = ArticleListingPageFactory(parent=root_page)
    article_page = ArticlePageFactory(parent=listing_page)

    editors = GroupFactory()
    editors.permissions.add(Permission.objects.get(codename='access_admin'))
    moderators = GroupFactory()
    moderators.permissions.add(Permission.objects.get(codename='access_admin'))

    for permission in editor_permissions:
        GroupPagePermissionFactory(
            page=listing_page, group=editors, permission_type=permission)
    for permission in moderator_permissions:
        GroupPagePermissionFactory(
            page=listing_page, group=moderators, permission_type=permission)

    editor = UserFactory(
        is_superuser=editor_is_superuser,
        is_staff=editor_is_staff,
        groups=[editors],
    )
    editor_password = editor_password or 'test'
    editor.set_password(editor_password)
    editor.save()

    moderator = UserFactory(
        is_superuser=moderator_is_superuser,
        is_staff=moderator_is_staff,
        groups=[moderators],
    )
    moderator_password = moderator_password or 'test'
    moderator.set_password(moderator_password)
    moderator.save()

    editor_client = Client()
    editor_client.login(username=editor.username, password=editor_password)
    moderator_client = Client()
    moderator_client.login(
        username=moderator.username,
        password=moderator_password
    )

    return BranchEditorAndModerator(
        listing_page,
        article_page,
        editors,
        editor,
        editor_client,
        moderators,
        moderator,
        moderator_client
    )


class BranchEditorFactory:
    @staticmethod
    def get(root_page, *, permissions=['add', 'edit'], **kwargs):
        return create_listing_with_article_and_group_with_user_and_client(
            root_page,
            permissions=permissions,
            **kwargs,
        )


class BranchModeratorFactory:
    @staticmethod
    def get(root_page, *, permissions=['add', 'edit', 'publish'], **kwargs):
        return create_listing_with_article_and_group_with_user_and_client(
            root_page,
            permissions=permissions,
            **kwargs,
        )


class BranchEditorAndModeratorFactory:
    @staticmethod
    def get(root_page, **kwargs):
        return create_listing_with_article_and_group_with_editor_and_moderator(
            root_page,
            **kwargs
        )

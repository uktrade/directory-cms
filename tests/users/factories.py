from collections import namedtuple

import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()
Branch = namedtuple(
    'Branch', ['listing', 'article', 'group', 'user', 'client']
)
TwoBranchesWithEditorModeratorAdmin = namedtuple(
    'TwoBranchesWithEditorModeratorAdmin', [
        'admins',
        'admin',
        'admin_client',
        'home_1',
        'landing_1',
        'listing_1',
        'article_1',
        'editors_1',
        'editor_1',
        'editor_1_client',
        'moderators_1',
        'moderator_1',
        'moderator_1_client',
        'home_2',
        'landing_2',
        'listing_2',
        'article_2',
        'editors_2',
        'editor_2',
        'editor_2_client',
        'moderators_2',
        'moderator_2',
        'moderator_2_client',
    ]
)


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n: "group %s" % n)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user %s" % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_superuser = False
    is_staff = False
    email = factory.Faker('email')

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)

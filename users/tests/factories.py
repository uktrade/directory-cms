import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from wagtail.core.models import GroupPagePermission, \
    PAGE_PERMISSION_TYPE_CHOICES

from export_readiness.tests.factories import ArticleListingPageFactory


User = get_user_model()


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n: "group %s" % n)


class GroupPagePermissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupPagePermission

    group = factory.SubFactory(GroupFactory)
    page = factory.SubFactory(ArticleListingPageFactory)
    permission_type = factory.fuzzy.FuzzyChoice(PAGE_PERMISSION_TYPE_CHOICES)


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

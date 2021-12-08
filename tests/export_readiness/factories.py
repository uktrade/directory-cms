import factory
import factory.fuzzy
import wagtail_factories

from export_readiness import snippets


class TagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.Tag

    name = factory.fuzzy.FuzzyText(length=10)


class IndustryTagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.IndustryTag

    name = factory.fuzzy.FuzzyText(length=10)
    icon = factory.SubFactory(wagtail_factories.ImageFactory)


class RegionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.Region

    name = factory.fuzzy.FuzzyText(length=10)


class CountryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.Country

    name = factory.fuzzy.FuzzyText(length=10)
    slug = factory.fuzzy.FuzzyText(length=10)

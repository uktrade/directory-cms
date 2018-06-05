import factory
import factory.fuzzy
import wagtail_factories

from invest import models


class InfoPageFactory(wagtail_factories.PageFactory):
    content_en_gb = factory.fuzzy.FuzzyText(length=10)
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class InvestHomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InvestHomePage

    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    sub_heading = factory.fuzzy.FuzzyText(length=100)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    slug_en_gb = 'invest-home'
    parent = None


class SectorPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.SectorPage

    description_en_gb = factory.fuzzy.FuzzyText(length=100)
    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class SetupGuidePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.SetupGuidePage

    description_en_gb = factory.fuzzy.FuzzyText(length=100)
    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    sub_heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None

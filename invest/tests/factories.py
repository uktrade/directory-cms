import factory
import factory.fuzzy
import wagtail_factories

from invest import models


class InfoPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InfoPage

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
    subsection_title_one_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_content_one_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_title_two_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_content_two_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_one_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_two_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_three_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_four_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_five_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_six_en_gb = 'http://test.com'
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
    pullout_text_en_gb = factory.fuzzy.FuzzyText(length=10)
    pullout_stat_en_gb = factory.fuzzy.FuzzyText(length=10)
    pullout_stat_text_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_title_one_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_content_one_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_title_two_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_content_two_en_gb = factory.fuzzy.FuzzyText(length=10)
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class RegionLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.RegionLandingPage

    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )


class SectorLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.SectorLandingPage

    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )


class SetupGuideLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.SetupGuideLandingPage

    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    sub_heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    lead_in_en_gb = factory.fuzzy.FuzzyText(length=10)
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class SetupGuidePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.SetupGuidePage

    description_en_gb = factory.fuzzy.FuzzyText(length=100)
    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    sub_heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    subsection_title_one_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_content_one_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_title_two_en_gb = factory.fuzzy.FuzzyText(length=10)
    subsection_content_two_en_gb = factory.fuzzy.FuzzyText(length=10)
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None

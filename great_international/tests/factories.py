import factory
import factory.fuzzy
import wagtail_factories
from django.utils import timezone

from great_international import models


class InternationalSectorPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalSectorPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None

    heading = factory.fuzzy.FuzzyText(length=10)
    sub_heading = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    heading_teaser = factory.fuzzy.FuzzyText(length=10)

    section_one_body = factory.fuzzy.FuzzyText(length=10)
    section_one_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )

    statistic_number_one = factory.fuzzy.FuzzyText(length=10)
    statistic_heading_one = factory.fuzzy.FuzzyText(length=10)
    statistic_smallprint_one = factory.fuzzy.FuzzyText(length=10)

    statistic_number_two = factory.fuzzy.FuzzyText(length=10)
    statistic_heading_two = factory.fuzzy.FuzzyText(length=10)
    statistic_smallprint_two = factory.fuzzy.FuzzyText(length=10)

    section_two_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_teaser = factory.fuzzy.FuzzyText(length=10)
    section_two_heading_one = factory.fuzzy.FuzzyText(length=10)
    section_two_body_one = factory.fuzzy.FuzzyText(length=10)
    section_two_heading_two = factory.fuzzy.FuzzyText(length=10)
    section_two_body_two = factory.fuzzy.FuzzyText(length=10)
    section_two_heading_three = factory.fuzzy.FuzzyText(length=10)
    section_two_body_three = factory.fuzzy.FuzzyText(length=10)

    case_study_title = factory.fuzzy.FuzzyText(length=10)
    case_study_description = factory.fuzzy.FuzzyText(length=10)
    case_study_cta_text = factory.fuzzy.FuzzyText(length=10)
    case_study_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )

    section_three_heading = factory.fuzzy.FuzzyText(length=10)
    section_three_teaser = factory.fuzzy.FuzzyText(length=10)
    section_three_heading_one = factory.fuzzy.FuzzyText(length=10)
    section_three_teaser_one = factory.fuzzy.FuzzyText(length=10)
    section_three_heading_two = factory.fuzzy.FuzzyText(length=10)
    section_three_teaser_two = factory.fuzzy.FuzzyText(length=10)

    next_steps_heading = factory.fuzzy.FuzzyText(length=10)
    next_steps_description = factory.fuzzy.FuzzyText(length=10)


class InternationalHomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalHomePage

    news_title = factory.fuzzy.FuzzyText(length=10)
    tariffs_title = factory.fuzzy.FuzzyText(length=10)
    tariffs_link = 'http://foo.com'
    tariffs_description = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class InternationalMarketingPagesFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalMarketingPages

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class InternationalArticleListingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalArticleListingPage

    landing_page_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class InternationalArticlePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalArticlePage

    article_title = factory.fuzzy.FuzzyText(length=10)
    article_teaser = factory.fuzzy.FuzzyText(length=10)
    article_body_text = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class InternationalCampaignPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalCampaignPage

    campaign_teaser = factory.fuzzy.FuzzyText(length=10)
    campaign_heading = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None
    section_one_heading = factory.fuzzy.FuzzyText(length=10)
    section_one_intro = factory.fuzzy.FuzzyText(length=10)
    selling_point_one_heading = factory.fuzzy.FuzzyText(length=10)
    selling_point_one_content = factory.fuzzy.FuzzyText(length=10)
    section_two_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_intro = factory.fuzzy.FuzzyText(length=10)
    related_content_heading = factory.fuzzy.FuzzyText(length=10)
    related_content_intro = factory.fuzzy.FuzzyText(length=10)
    cta_box_message = factory.fuzzy.FuzzyText(length=10)
    cta_box_button_url = factory.fuzzy.FuzzyText(length=10)
    cta_box_button_text = factory.fuzzy.FuzzyText(length=10)


class InternationalTopicLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalTopicLandingPage

    landing_page_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class InternationalRegionPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalRegionPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class InternationalRegionalFolderPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalRegionalFolderPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = factory.SubFactory(InternationalRegionPageFactory)

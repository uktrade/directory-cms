import factory
import factory.fuzzy
import string
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
    section_one_image_caption = factory.fuzzy.FuzzyText(length=10)
    section_one_image_caption_company = factory.fuzzy.FuzzyText(length=10)

    statistic_1_number = factory.fuzzy.FuzzyText(length=10)
    statistic_1_heading = factory.fuzzy.FuzzyText(length=10)
    statistic_1_smallprint = factory.fuzzy.FuzzyText(length=10)

    statistic_2_number = factory.fuzzy.FuzzyText(length=10)
    statistic_2_heading = factory.fuzzy.FuzzyText(length=10)
    statistic_2_smallprint = factory.fuzzy.FuzzyText(length=10)

    statistic_3_number = factory.fuzzy.FuzzyText(length=10)
    statistic_3_heading = factory.fuzzy.FuzzyText(length=10)
    statistic_3_smallprint = factory.fuzzy.FuzzyText(length=10)

    statistic_4_number = factory.fuzzy.FuzzyText(length=10)
    statistic_4_heading = factory.fuzzy.FuzzyText(length=10)
    statistic_4_smallprint = factory.fuzzy.FuzzyText(length=10)

    statistic_5_number = factory.fuzzy.FuzzyText(length=10)
    statistic_5_heading = factory.fuzzy.FuzzyText(length=10)
    statistic_5_smallprint = factory.fuzzy.FuzzyText(length=10)

    statistic_6_number = factory.fuzzy.FuzzyText(length=10)
    statistic_6_heading = factory.fuzzy.FuzzyText(length=10)
    statistic_6_smallprint = factory.fuzzy.FuzzyText(length=10)

    section_two_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_teaser = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_one_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    section_two_subsection_one_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_one_body = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_two_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    section_two_subsection_two_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_two_body = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_three_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    section_two_subsection_three_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_three_body = factory.fuzzy.FuzzyText(length=10)

    case_study_title = factory.fuzzy.FuzzyText(length=10)
    case_study_description = factory.fuzzy.FuzzyText(length=10)
    case_study_cta_text = factory.fuzzy.FuzzyText(length=10)
    case_study_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )

    section_three_heading = factory.fuzzy.FuzzyText(length=10)
    section_three_teaser = factory.fuzzy.FuzzyText(length=10)
    section_three_subsection_one_heading = factory.fuzzy.FuzzyText(length=10)
    section_three_subsection_one_teaser = factory.fuzzy.FuzzyText(length=10)
    section_three_subsection_one_body = factory.fuzzy.FuzzyText(length=10)
    section_three_subsection_two_heading = factory.fuzzy.FuzzyText(length=10)
    section_three_subsection_two_teaser = factory.fuzzy.FuzzyText(length=10)
    section_three_subsection_two_body = factory.fuzzy.FuzzyText(length=10)


class InternationalHomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalHomePage

    hero_title = factory.fuzzy.FuzzyText(length=10)
    invest_title = factory.fuzzy.FuzzyText(length=10)
    trade_title = factory.fuzzy.FuzzyText(length=10)
    section_two_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_teaser = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_one_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_one_body = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_one_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    section_two_subsection_two_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_two_body = factory.fuzzy.FuzzyText(length=10)
    section_two_subsection_two_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    tariffs_call_to_action_text = factory.fuzzy.FuzzyText(length=10)
    study_in_uk_cta_text = factory.fuzzy.FuzzyText(length=10)
    visit_uk_cta_text = factory.fuzzy.FuzzyText(length=10)
    news_title = factory.fuzzy.FuzzyText(length=10)
    tariffs_title = factory.fuzzy.FuzzyText(length=10)
    tariffs_link = 'http://foo.com'
    tariffs_description = factory.fuzzy.FuzzyText(length=10)
    featured_link_one_heading = factory.fuzzy.FuzzyText(length=10)
    featured_link_one_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
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


class fuzzyURL(factory.fuzzy.BaseFuzzyAttribute):
    def __init__(self, protocol='https', tld='co.uk', name_length=15):
        super().__init__()
        self.protocol = protocol
        self.tld = tld
        self.name_length = name_length

    def fuzz(self):
        chars = [
            factory.fuzzy._random.choice(string.ascii_lowercase)
            for _i in range(self.name_length)
        ]
        return self.protocol + '://' + ''.join(chars) + '.' + self.tld


class InternationalCuratedTopicLandingPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.InternationalCuratedTopicLandingPage

    display_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    teaser = factory.fuzzy.FuzzyText(length=10)
    feature_section_heading = factory.fuzzy.FuzzyText(length=10)
    parent = None
    # Large features
    feature_one_heading = factory.fuzzy.FuzzyText(length=10)
    feature_one_image = factory.SubFactory(wagtail_factories.ImageFactory)
    feature_one_content = factory.fuzzy.FuzzyText(length=10)
    feature_two_heading = factory.fuzzy.FuzzyText(length=10)
    feature_two_image = factory.SubFactory(wagtail_factories.ImageFactory)
    feature_two_content = factory.fuzzy.FuzzyText(length=10)
    # Small features
    feature_three_heading = factory.fuzzy.FuzzyText(length=10)
    feature_three_image = factory.SubFactory(wagtail_factories.ImageFactory)
    feature_three_url = fuzzyURL()
    feature_four_heading = factory.fuzzy.FuzzyText(length=10)
    feature_four_image = factory.SubFactory(wagtail_factories.ImageFactory)
    feature_four_url = fuzzyURL()
    feature_five_heading = factory.fuzzy.FuzzyText(length=10)
    feature_five_image = factory.SubFactory(wagtail_factories.ImageFactory)
    feature_five_url = fuzzyURL()


class InternationalGuideLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalGuideLandingPage

    display_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(wagtail_factories.ImageFactory)
    teaser = factory.fuzzy.FuzzyText(length=10)

    section_one_content = factory.fuzzy.FuzzyText(length=10)
    section_one_image = factory.SubFactory(wagtail_factories.ImageFactory)
    section_one_image_caption = factory.fuzzy.FuzzyText(length=10)

    section_two_heading = factory.fuzzy.FuzzyText(length=10)
    section_two_teaser = factory.fuzzy.FuzzyText(length=10)
    section_two_button_text = factory.fuzzy.FuzzyText(length=10)
    section_two_button_url = factory.fuzzy.FuzzyText(length=10)
    section_two_image = factory.SubFactory(wagtail_factories.ImageFactory)
    guides_section_heading = factory.fuzzy.FuzzyText(length=10)

    parent = None


class InternationalRegionPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalRegionPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class InternationalLocalisedFolderPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalLocalisedFolderPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = factory.SubFactory(InternationalRegionPageFactory)


class InternationalCapitalInvestLandingPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.InternationalCapitalInvestLandingPage

    hero_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class CapitalInvestRegionPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.CapitalInvestRegionPage

    hero_title = factory.fuzzy.FuzzyText(length=10)
    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    featured_description = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class CapitalInvestRegionalSectorPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.CapitalInvestRegionalSectorPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    hero_title = factory.fuzzy.FuzzyText(length=10)
    featured_description = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()


class CapitalInvestOpportunityPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.CapitalInvestOpportunityPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    hero_title = factory.fuzzy.FuzzyText(length=10)
    location = factory.fuzzy.FuzzyText(length=10)
    scale = factory.fuzzy.FuzzyText(length=10)
    investment_type = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class CapitalInvestOpportunityListingPageFactory(
    wagtail_factories.PageFactory
):
    class Meta:
        model = models.CapitalInvestOpportunityListingPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None

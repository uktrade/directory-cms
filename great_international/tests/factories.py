import factory
import factory.fuzzy
import string
import wagtail_factories
from django.utils import timezone

from great_international import models


class GreatInternationalAppFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.GreatInternationalApp

    title = factory.Sequence(lambda n: '123-555-{0}'.format(n))


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


class InvestInternationalHomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InvestInternationalHomePage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    sub_heading = factory.fuzzy.FuzzyText(length=100)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    benefits_section_title = factory.fuzzy.FuzzyText(length=10)
    capital_invest_section_title = factory.fuzzy.FuzzyText(length=10)
    sector_title = factory.fuzzy.FuzzyText(length=10)
    sector_button_text = factory.fuzzy.FuzzyText(length=10)
    sector_button_url = factory.fuzzy.FuzzyText(length=10)
    hpo_title = factory.fuzzy.FuzzyText(length=10)
    setup_guide_title = factory.fuzzy.FuzzyText(length=10)
    setup_guide_call_to_action_url = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_one_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_two_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_three_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_four_en_gb = factory.fuzzy.FuzzyText(length=10)
    how_we_help_text_five_en_gb = factory.fuzzy.FuzzyText(length=10)
    contact_section_title = factory.fuzzy.FuzzyText(length=10)
    contact_section_call_to_action_text = factory.fuzzy.FuzzyText(length=10)
    contact_section_call_to_action_url = factory.fuzzy.FuzzyText(length=10)
    slug = 'invest-home'
    parent = None


class InvestHighPotentialOpportunityFormPageFactory(
    wagtail_factories.PageFactory
):
    class Meta:
        model = models.InvestHighPotentialOpportunityFormPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    heading = factory.fuzzy.FuzzyText(length=200)
    sub_heading = factory.fuzzy.FuzzyText(length=200)
    comment_help_text = factory.fuzzy.FuzzyText(length=200)
    comment_label = factory.fuzzy.FuzzyText(length=200)
    company_name_help_text = factory.fuzzy.FuzzyText(length=200)
    company_name_label = factory.fuzzy.FuzzyText(length=200)
    company_size_help_text = factory.fuzzy.FuzzyText(length=200)
    company_size_label = factory.fuzzy.FuzzyText(length=200)
    country_help_text = factory.fuzzy.FuzzyText(length=200)
    country_label = factory.fuzzy.FuzzyText(length=200)
    email_address_help_text = factory.fuzzy.FuzzyText(length=200)
    email_address_label = factory.fuzzy.FuzzyText(length=200)
    full_name_help_text = factory.fuzzy.FuzzyText(length=200)
    full_name_label = factory.fuzzy.FuzzyText(length=200)
    opportunities_help_text = factory.fuzzy.FuzzyText(length=200)
    opportunities_label = factory.fuzzy.FuzzyText(length=200)
    phone_number_help_text = factory.fuzzy.FuzzyText(length=200)
    phone_number_label = factory.fuzzy.FuzzyText(length=200)
    role_in_company_help_text = factory.fuzzy.FuzzyText(length=200)
    role_in_company_label = factory.fuzzy.FuzzyText(length=200)
    website_url_help_text = factory.fuzzy.FuzzyText(length=200)
    website_url_label = factory.fuzzy.FuzzyText(length=200)
    parent = None


class InvestHighPotentialOpportunityDetailPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.InvestHighPotentialOpportunityDetailPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=50)
    heading = factory.fuzzy.FuzzyText(length=50)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    contact_proposition = factory.fuzzy.FuzzyText(length=50)
    contact_button = factory.fuzzy.FuzzyText(length=50)
    proposition_one = factory.fuzzy.FuzzyText(length=50)
    opportunity_list_title = factory.fuzzy.FuzzyText(length=50)
    opportunity_list_item_one = factory.fuzzy.FuzzyText(length=50)
    opportunity_list_item_two = factory.fuzzy.FuzzyText(length=50)
    opportunity_list_item_three = factory.fuzzy.FuzzyText(length=50)
    opportunity_list_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    proposition_two = factory.fuzzy.FuzzyText(length=50)
    proposition_two_list_item_one = factory.fuzzy.FuzzyText(length=50)
    proposition_two_list_item_two = factory.fuzzy.FuzzyText(length=50)
    proposition_two_list_item_three = factory.fuzzy.FuzzyText(length=50)
    proposition_two_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    competitive_advantages_title = factory.fuzzy.FuzzyText(length=50)
    competitive_advantages_list_item_one = factory.fuzzy.FuzzyText(length=50)
    competitive_advantages_list_item_one_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    competitive_advantages_list_item_two = factory.fuzzy.FuzzyText(length=50)
    competitive_advantages_list_item_two_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    competitive_advantages_list_item_three = factory.fuzzy.FuzzyText(length=50)
    competitive_advantages_list_item_three_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    testimonial = factory.fuzzy.FuzzyText(length=50)
    companies_list_text = factory.fuzzy.FuzzyText(length=50)
    companies_list_item_image_one = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    companies_list_item_image_two = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    companies_list_item_image_three = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    companies_list_item_image_four = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    companies_list_item_image_five = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    companies_list_item_image_six = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    companies_list_item_image_seven = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    companies_list_item_image_eight = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    case_study_list_title = factory.fuzzy.FuzzyText(length=50)
    case_study_one_text = factory.fuzzy.FuzzyText(length=50)
    case_study_one_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    case_study_two_text = factory.fuzzy.FuzzyText(length=50)
    case_study_two_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    case_study_three_text = factory.fuzzy.FuzzyText(length=50)
    case_study_three_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    case_study_four_text = factory.fuzzy.FuzzyText(length=50)
    case_study_four_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    other_opportunities_title = factory.fuzzy.FuzzyText(length=50)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None

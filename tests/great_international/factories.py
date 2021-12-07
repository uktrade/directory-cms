import random
import string

import factory
import factory.fuzzy
import wagtail_factories

from django.utils import timezone

from great_international import models


class InternationalSectorPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.great_international.InternationalSectorPage

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


class InternationalSubSectorPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.great_international.InternationalSubSectorPage

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
        model = models.great_international.InternationalHomePage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None

    hero_title = factory.fuzzy.FuzzyText(length=10)
    # homepage_link_panels is a StreamField


class InternationalArticleListingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.great_international.InternationalArticleListingPage

    landing_page_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class InternationalArticlePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.great_international.InternationalArticlePage

    type_of_article = 'Blog'

    article_title = factory.fuzzy.FuzzyText(length=10)
    article_subheading = factory.fuzzy.FuzzyText(length=10)
    article_teaser = factory.fuzzy.FuzzyText(length=10)

    article_image = factory.SubFactory(wagtail_factories.ImageFactory)

    article_body_text = factory.fuzzy.FuzzyText(length=10)

    cta_title = factory.fuzzy.FuzzyText(length=10)
    cta_teaser = factory.fuzzy.FuzzyText(length=10)
    cta_link_label = factory.fuzzy.FuzzyText(length=10)
    cta_link = factory.fuzzy.FuzzyText(length=10)

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class InternationalCampaignPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.great_international.InternationalCampaignPage

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
        model = models.great_international.InternationalTopicLandingPage

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
            random.choice(string.ascii_lowercase)
            for _i in range(self.name_length)
        ]
        return self.protocol + '://' + ''.join(chars) + '.' + self.tld


class InternationalGuideLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.great_international.InternationalGuideLandingPage

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


class InternationalCapitalInvestLandingPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.capital_invest.InternationalCapitalInvestLandingPage

    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class CapitalInvestRegionPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.capital_invest.CapitalInvestRegionPage

    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    featured_description = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class CapitalInvestOpportunityPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.capital_invest.CapitalInvestOpportunityPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    project_background_title = factory.fuzzy.FuzzyText(length=10)
    project_background_intro = factory.fuzzy.FuzzyText(length=10)
    location = factory.fuzzy.FuzzyText(length=10)
    scale = factory.fuzzy.FuzzyText(length=10)
    investment_type = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class CapitalInvestRelatedSectorsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.capital_invest.CapitalInvestRelatedSectors

    page = None
    related_sector = None


class CapitalInvestOpportunityListingPageFactory(
    wagtail_factories.PageFactory
):
    class Meta:
        model = models.capital_invest.CapitalInvestOpportunityListingPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    search_results_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class InvestInternationalHomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.invest.InvestInternationalHomePage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    sub_heading = factory.fuzzy.FuzzyText(length=100)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    benefits_section_title = factory.fuzzy.FuzzyText(length=10)
    sector_title = factory.fuzzy.FuzzyText(length=10)
    sector_button_text = factory.fuzzy.FuzzyText(length=10)
    sector_button_url = factory.fuzzy.FuzzyText(length=10)
    hpo_title = factory.fuzzy.FuzzyText(length=10)
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


class InvestHighPotentialOpportunitiesPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.invest.InvestHighPotentialOpportunitiesPage

    parent = None


class ForeignDirectInvestmentFormPageFactory(
    wagtail_factories.PageFactory
):
    class Meta:
        model = models.investment_atlas.ForeignDirectInvestmentFormPage

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


class ForeignDirectInvestmentFormSuccessPageFactory(
    wagtail_factories.PageFactory
):
    class Meta:
        model = models.investment_atlas.ForeignDirectInvestmentFormSuccessPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    heading = factory.fuzzy.FuzzyText(length=200)
    sub_heading = factory.fuzzy.FuzzyText(length=200)
    next_steps_title = factory.fuzzy.FuzzyText(length=200)
    next_steps_body = factory.fuzzy.FuzzyText(length=200)
    documents_title = factory.fuzzy.FuzzyText(length=200)
    documents_body = factory.fuzzy.FuzzyText(length=200)
    parent = None


class InvestHighPotentialOpportunityDetailPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.invest.InvestHighPotentialOpportunityDetailPage

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


class InvestRegionPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.invest.InvestRegionPage

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
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class InvestRegionLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.invest.InvestRegionLandingPage

    heading_en_gb = factory.fuzzy.FuzzyText(length=100)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )


class InternationalTradeHomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.find_a_supplier.InternationalTradeHomePage

    hero_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    breadcrumbs_label_en_gb = factory.fuzzy.FuzzyText(length=50)
    search_field_placeholder_en_gb = factory.fuzzy.FuzzyText(length=255)
    search_button_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    proposition_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    call_to_action_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    industries_list_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    industries_list_call_to_action_text_en_gb = factory.fuzzy.FuzzyText(
        length=255
    )
    services_list_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    services_column_one_en_gb = factory.fuzzy.FuzzyText(length=255)
    services_column_two_en_gb = factory.fuzzy.FuzzyText(length=255)
    services_column_three_en_gb = factory.fuzzy.FuzzyText(length=255)
    services_column_four_en_gb = factory.fuzzy.FuzzyText(length=255)
    services_column_one_icon_en_gb = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    services_column_two_icon_en_gb = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    services_column_three_icon_en_gb = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    services_column_four_icon_en_gb = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    search_description_en_gb = factory.fuzzy.FuzzyText(length=255)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class InternationalTradeIndustryContactPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.find_a_supplier.InternationalTradeIndustryContactPage

    breadcrumbs_label_en_gb = factory.fuzzy.FuzzyText(length=50)
    introduction_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    submit_button_text_en_gb = factory.fuzzy.FuzzyText(length=100)
    success_message_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    success_back_link_text_en_gb = factory.fuzzy.FuzzyText(length=100)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class AboutDitServicesPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.great_international.AboutDitServicesPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=50)
    breadcrumbs_label_en_gb = factory.fuzzy.FuzzyText(length=50)
    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class AboutUkLandingPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.great_international.AboutUkLandingPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=50)
    breadcrumbs_label_en_gb = factory.fuzzy.FuzzyText(length=50)
    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class AboutUkRegionListingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.great_international.AboutUkRegionListingPage

    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class AboutUkRegionPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.great_international.AboutUkRegionPage

    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    featured_description = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class AboutUkWhyChooseTheUkPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.great_international.AboutUkWhyChooseTheUkPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=50)
    breadcrumbs_label_en_gb = factory.fuzzy.FuzzyText(length=50)
    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class CapitalInvestContactFormPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.capital_invest.CapitalInvestContactFormPage

    heading = factory.fuzzy.FuzzyText(length=50)
    intro = factory.fuzzy.FuzzyText(length=50)
    cta_text = factory.fuzzy.FuzzyText(length=50)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class CapitalInvestContactFormSuccessPageFactory(
    wagtail_factories.PageFactory
):

    class Meta:
        model = models.capital_invest.CapitalInvestContactFormSuccessPage

    message_box_heading = factory.fuzzy.FuzzyText(length=50)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class PlanningStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.investment_atlas.PlanningStatus

    name = factory.fuzzy.FuzzyText(length=30)
    verbose_description = factory.fuzzy.FuzzyText(length=200)


class InvestmentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.investment_atlas.InvestmentType

    name = factory.fuzzy.FuzzyText(length=30)


class InvestmentOpportunityPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.investment_atlas.InvestmentOpportunityPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    priority_weighting = '0.0'
    strapline = factory.fuzzy.FuzzyText(length=200)
    introduction = factory.fuzzy.FuzzyText(length=300)
    opportunity_summary = factory.fuzzy.FuzzyText(length=300)
    hero_image = factory.SubFactory(wagtail_factories.ImageFactory)
    intro_image = factory.SubFactory(wagtail_factories.ImageFactory)
    location = factory.fuzzy.FuzzyText(length=200)
    promoter = factory.fuzzy.FuzzyText(length=200)
    scale = factory.fuzzy.FuzzyText(length=255)
    scale_value = factory.fuzzy.FuzzyDecimal(low=1, high=99999)

    planning_status = factory.SubFactory(PlanningStatusFactory)
    investment_type = factory.SubFactory(InvestmentTypeFactory)
    time_to_investment_decision = models.investment_atlas.TIME_TO_INVESTMENT_DECISION_0M_6M

    # Streamfields - set them in the instance
    # main_content

    # regions_with_location - Added as streamfields which holds regions and map coordinates


class InvestmentOpportunityRelatedSectorsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.investment_atlas.InvestmentOpportunityRelatedSectors

    page = None
    related_sector = None


class InvestmentOpportunityListingPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.investment_atlas.InvestmentOpportunityListingPage

    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    search_results_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    hero_text = factory.fuzzy.FuzzyText(length=50)
    contact_cta_title = factory.fuzzy.FuzzyText(length=50)
    contact_cta_text = factory.fuzzy.FuzzyText(length=50)
    contact_cta_link = 'https://example.com/test/cta/'
    parent = None


class InvestmentAtlasLandingPageFactory(wagtail_factories.PageFactory):
    breadcrumbs_label = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))

    hero_title = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    parent = None

    class Meta:
        model = models.investment_atlas.InvestmentAtlasLandingPage


class ReusableContentSectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.investment_atlas.ReusableContentSection

    title = factory.fuzzy.FuzzyText(length=10)
    block_slug = factory.fuzzy.FuzzyText(length=10)
    # content is a StreamField, so easier to set in the test


class InternationalInvestmentSectorPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.great_international.InternationalInvestmentSectorPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None

    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    intro_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )

    heading = factory.fuzzy.FuzzyText(length=10)


class InternationalInvestmentSubSectorPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.great_international.InternationalInvestmentSubSectorPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None

    heading = factory.fuzzy.FuzzyText(length=10)

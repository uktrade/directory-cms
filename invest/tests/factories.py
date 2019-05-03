import factory
import factory.fuzzy
import wagtail_factories

from invest import models


class InvestAppFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InvestApp

    title = factory.Sequence(lambda n: '123-555-{0}'.format(n))


class InfoPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InfoPage

    content_en_gb = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class InvestHomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InvestHomePage

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
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
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
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
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
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class HighPotentialOpportunityFormPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.HighPotentialOpportunityFormPage

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


class HighPotentialOpportunityDetailPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.HighPotentialOpportunityDetailPage

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

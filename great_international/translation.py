from modeltranslation.decorators import register

from core.translation import BaseTranslationOptions
from great_international.models import capital_invest, find_a_supplier, great_international, investment_atlas


@register(great_international.InternationalArticlePage)
class InternationalArticlePageTranslationOptions(BaseTranslationOptions):
    fields = (
        'article_title',
        'article_subheading',
        'article_teaser',
        'article_body_text',
        'cta_title',
        'cta_teaser',
        'cta_link_label',
        'cta_link',
    )


@register(great_international.InternationalCampaignPage)
class InternationalCampaignPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'campaign_subheading',
        'campaign_teaser',
        'campaign_heading',
        'campaign_hero_image',
        'section_one_heading',
        'section_one_intro',
        'section_one_image',
        'selling_point_one_icon',
        'selling_point_one_heading',
        'selling_point_one_content',
        'selling_point_two_icon',
        'selling_point_two_heading',
        'selling_point_two_content',
        'selling_point_three_icon',
        'selling_point_three_heading',
        'selling_point_three_content',
        'section_one_contact_button_url',
        'section_one_contact_button_text',
        'section_two_heading',
        'section_two_intro',
        'section_two_image',
        'section_two_contact_button_url',
        'section_two_contact_button_text',
        'related_content_heading',
        'related_content_intro',
        'related_page_one',
        'related_page_two',
        'related_page_three',
        'cta_box_message',
        'cta_box_button_url',
        'cta_box_button_text',
    )


@register(great_international.InternationalHomePage)
class InternationalHomePageTranslationOptions(BaseTranslationOptions):
    fields = (
        'hero_title',
        'hero_video',
        'homepage_link_panels',
    )


@register(great_international.InternationalArticleListingPage)
class InternationalArticleListingPage(BaseTranslationOptions):
    fields = (
        'landing_page_title',
        'hero_image',
        'hero_teaser',
        'list_teaser',
    )


@register(great_international.InternationalTopicLandingPage)
class InternationalTopicLandingPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'landing_page_title',
        'hero_video',
        'hero_image',
        'hero_teaser',
        'related_page_one',
        'related_page_two',
        'related_page_three',
    )


@register(investment_atlas.ForeignDirectInvestmentFormPage)
class ForeignDirectInvestmentFormPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(investment_atlas.ForeignDirectInvestmentFormSuccessPage)
class ForeignDirectInvestmentFormSuccessPageTranslationOptions(
    BaseTranslationOptions
):
    fields = []


@register(find_a_supplier.InternationalTradeHomePage)
class InternationalTradeHomePageTranslationOptions(BaseTranslationOptions):
    fields = (
        'breadcrumbs_label',
        'hero_text',
        'hero_image_caption',
        'search_field_placeholder',
        'search_button_text',
        'proposition_text',
        'call_to_action_text',
        'industries_list_text',
        'industries_list_call_to_action_text',
        'services_list_text',
        'services_column_one',
        'services_column_two',
        'services_column_three',
        'services_column_four',
        'services_column_one_icon',
        'services_column_two_icon',
        'services_column_three_icon',
        'services_column_four_icon',
        'how_we_help_cta_text',
        'how_we_help_cta_link',
    )


@register(find_a_supplier.InternationalTradeIndustryContactPage)
class InternationalTradeIndustryContactPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'introduction_text',
        'submit_button_text',
        'success_message_text',
        'success_back_link_text',
    )


@register(great_international.AboutDitServicesPage)
class AboutDitServicesPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'hero_title',
        'featured_description',
        'teaser',

        'ebook_section_image_alt_text',
        'ebook_section_body',
        'ebook_section_cta_text',
        'ebook_section_cta_link',

        'case_study_title',
        'case_study_text',
        'case_study_cta_text',
        'case_study_cta_link',
        'contact_us_section_title',
        'contact_us_section_summary',
        'contact_us_section_cta_text',
        'contact_us_section_cta_link',
    )


@register(great_international.AboutDitServicesFields)
class AboutDitServicesFieldsTranslationOptions(
        BaseTranslationOptions
):
    fields = (
        'page',
    )


@register(great_international.AboutUkRegionListingPage)
class AboutUkRegionListingPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'hero_title',

        'intro',

        'contact_title',
        'contact_text',
        'contact_cta_text',
        'contact_cta_link',
        'related_page_one',
        'related_page_two',
        'related_page_three',
    )


@register(great_international.AboutUkRegionPage)
class AboutUkRegionPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'hero_title',
        'breadcrumbs_label',
        'hero_image',

        'featured_description',

        'region_summary_section_image',
        'region_summary_section_strapline',
        'region_summary_section_intro',
        'region_summary_section_content',

        'investment_opps_title',
        'investment_opps_intro',

        'economics_data_title',
        'economics_stat_1_number',
        'economics_stat_1_heading',
        'economics_stat_1_smallprint',

        'economics_stat_2_number',
        'economics_stat_2_heading',
        'economics_stat_2_smallprint',

        'economics_stat_3_number',
        'economics_stat_3_heading',
        'economics_stat_3_smallprint',

        'economics_stat_4_number',
        'economics_stat_4_heading',
        'economics_stat_4_smallprint',

        'economics_stat_5_number',
        'economics_stat_5_heading',
        'economics_stat_5_smallprint',

        'economics_stat_6_number',
        'economics_stat_6_heading',
        'economics_stat_6_smallprint',

        'location_data_title',
        'location_stat_1_number',
        'location_stat_1_heading',
        'location_stat_1_smallprint',

        'location_stat_2_number',
        'location_stat_2_heading',
        'location_stat_2_smallprint',

        'location_stat_3_number',
        'location_stat_3_heading',
        'location_stat_3_smallprint',

        'location_stat_4_number',
        'location_stat_4_heading',
        'location_stat_4_smallprint',

        'location_stat_5_number',
        'location_stat_5_heading',
        'location_stat_5_smallprint',

        'location_stat_6_number',
        'location_stat_6_heading',
        'location_stat_6_smallprint',

        'subsections_title',

        'sub_section_one_title',
        'sub_section_one_icon',
        'sub_section_one_content',

        'sub_section_two_title',
        'sub_section_two_icon',
        'sub_section_two_content',

        'sub_section_three_title',
        'sub_section_three_icon',
        'sub_section_three_content',

        'property_and_infrastructure_section_title',
        'property_and_infrastructure_section_image',
        'property_and_infrastructure_section_content',

        'case_study_image',
        'case_study_title',
        'case_study_text',
        'case_study_cta_text',
        'case_study_cta_link',

        'contact_title',
        'contact_text',
        'contact_cta_link',
        'contact_cta_text',

    )


@register(capital_invest.CapitalInvestContactFormPage)
class CapitalInvestContactFormPageTranslationOptions(
        BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'heading',
        'intro',
        'comment',
        'cta_text',
    )


@register(capital_invest.CapitalInvestContactFormSuccessPage)
class CapitalInvestContactFormSuccessPageTranslationOptions(
        BaseTranslationOptions
):
    fields = (
        'message_box_heading',
        'message_box_description',
        'what_happens_next_description',
    )


@register(investment_atlas.InvestmentAtlasLandingPage)
class InvestmentAtlasLandingPageTranslationOptions(
    BaseTranslationOptions,
):
    fields = (
        'breadcrumbs_label',
        'hero_title',
        'hero_image',
        'mobile_hero_image',
        'hero_video',
        'hero_strapline',
        'hero_cta_text',
        'hero_cta_link',
        'downpage_sections',
    )


@register(investment_atlas.InvestmentOpportunityListingPage)
class InvestmentOpportunityListingPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'search_results_title',
        'hero_video',
        'hero_text',
        'contact_cta_title',
        'contact_cta_text',
        'contact_cta_link',
    )


@register(investment_atlas.InvestmentOpportunityPage)
class InvestmentOpportunityPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'breadcrumbs_label',
        'hero_image',
        'hero_video',
        'strapline',
        'introduction',
        'intro_image',
        'intro_video',
        'opportunity_summary',
        'promoter',
        'location',
        'scale',
        'scale_value',
        'planning_status',
        'investment_type',
        'time_to_investment_decision',
        'main_content',
        'important_links',
        'contact_name',
        'contact_avatar',
        'contact_job_title',
        'contact_link'
    )


@register(great_international.InternationalInvestmentSectorPage)
class InternationalInvestmentSectorPageTranslationOptions(
    BaseTranslationOptions
):
    fields = (
        'hero_image',
        'hero_video',
        'heading',
        'standfirst',
        'featured_description',
        'intro_text',
        'intro_image',
        'contact_name',
        'contact_avatar',
        'contact_job_title',
        'contact_link',
        'contact_link_button_preamble',
        'contact_link_button_label',
        'related_opportunities_header',
        'downpage_content',
        'early_opportunities_header',
        'early_opportunities',
    )


@register(great_international.InternationalInvestmentSubSectorPage)
class InternationalInvestmentSubSectorPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'heading',
    )


@register(great_international.WhyInvestInTheUKPage)
class InternationalWhyInvestInTheUKPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'hero_image',
        'hero_video',
        'strapline',
        'introduction',
        'intro_image',
        'uk_strength_title',
        'uk_strength_intro',
        'uk_strength_panels',
    )


@register(investment_atlas.InvestmentGeneralContentPage)
class InvestmentGeneralContentPageTranslationOptions(BaseTranslationOptions):
    fields = (
        'hero_image',
        'hero_video',
        'strapline',
        'introduction',
        'intro_image',
        'main_content',
    )

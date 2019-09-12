import factory
import factory.fuzzy
import wagtail_factories
from django.utils import timezone

from export_readiness import models, snippets


class SitePolicyPagesFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.SitePolicyPages

    title = factory.Sequence(lambda n: '123-555-{0}'.format(n))


class PerformanceDashboardPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.PerformanceDashboardPage

    heading = factory.fuzzy.FuzzyText(length=10)
    description = factory.fuzzy.FuzzyText(length=10)
    product_link = 'http://www.foo.bar'
    # row 1
    data_title_row_one = factory.fuzzy.FuzzyText(length=10)
    data_number_row_one = factory.fuzzy.FuzzyText(length=10)
    data_period_row_one = factory.fuzzy.FuzzyText(length=10)
    data_description_row_one = factory.fuzzy.FuzzyText(length=10)
    # row 2
    data_title_row_two = factory.fuzzy.FuzzyText(length=10)
    data_number_row_two = factory.fuzzy.FuzzyText(length=10)
    data_period_row_two = factory.fuzzy.FuzzyText(length=10)
    data_description_row_two = factory.fuzzy.FuzzyText(length=10)
    # row 3
    data_title_row_three = factory.fuzzy.FuzzyText(length=10)
    data_number_row_three = factory.fuzzy.FuzzyText(length=10)
    data_period_row_three = factory.fuzzy.FuzzyText(length=10)
    data_description_row_three = factory.fuzzy.FuzzyText(length=10)

    guidance_notes = factory.fuzzy.FuzzyText(length=200)
    landing_dashboard = False

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class PerformanceDashboardNotesPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.PerformanceDashboardNotesPage

    body = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class TopicLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.TopicLandingPage

    landing_page_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class SuperregionPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.SuperregionPage

    landing_page_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class ArticleListingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.ArticleListingPage

    landing_page_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class CampaignPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.CampaignPage

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


class ArticlePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.ArticlePage

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


class MarketingArticlePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.MarketingArticlePage

    article_title = factory.fuzzy.FuzzyText(length=10)
    article_teaser = factory.fuzzy.FuzzyText(length=10)
    article_body_text = factory.fuzzy.FuzzyText(length=10)
    cta_title = factory.fuzzy.FuzzyText(length=10)
    cta_teaser = factory.fuzzy.FuzzyText(length=10)
    cta_link_label = factory.fuzzy.FuzzyText(length=10)
    cta_link = factory.fuzzy.FuzzyText(length=255)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class TagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.Tag

    name = factory.fuzzy.FuzzyText(length=10)


class HomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.HomePage

    news_title = factory.fuzzy.FuzzyText(length=10)
    news_description = factory.fuzzy.FuzzyText(length=10)
    banner_content = factory.fuzzy.FuzzyText(length=10)
    banner_label = factory.fuzzy.FuzzyText(length=10)

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class HomePageOldFactory(HomePageFactory):

    class Meta:
        model = models.HomePageOld


class InternationaLandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.InternationalLandingPage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class ContactUsGuidancePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.ContactUsGuidancePage

    last_published_at = timezone.now()
    parent = None
    body = factory.fuzzy.FuzzyText(length=50)


class ContactSuccessPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.ContactSuccessPage

    heading = factory.fuzzy.FuzzyText(length=50)
    body_text = factory.fuzzy.FuzzyText(length=50)
    next_title = factory.fuzzy.FuzzyText(length=50)
    next_body_text = factory.fuzzy.FuzzyText(length=50)
    parent = None


class PrivacyAndCookiesPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.PrivacyAndCookiesPage

    body = factory.fuzzy.FuzzyText(length=50)


class CountryGuidePageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.CountryGuidePage

    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None

    heading = factory.fuzzy.FuzzyText(length=10)
    sub_heading = factory.fuzzy.FuzzyText(length=10)
    heading_teaser = factory.fuzzy.FuzzyText(length=10)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    intro_cta_one_title = factory.fuzzy.FuzzyText(length=10)
    intro_cta_one_link = factory.fuzzy.FuzzyText(length=10)
    intro_cta_two_title = factory.fuzzy.FuzzyText(length=10)
    intro_cta_two_link = factory.fuzzy.FuzzyText(length=10)
    intro_cta_three_title = factory.fuzzy.FuzzyText(length=10)
    intro_cta_three_link = factory.fuzzy.FuzzyText(length=10)
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

    accordion_1_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    accordion_1_title = factory.fuzzy.FuzzyText(length=10)
    accordion_1_teaser = factory.fuzzy.FuzzyText(length=10)

    accordion_1_subsection_1_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    accordion_1_subsection_1_heading = factory.fuzzy.FuzzyText(length=10)
    accordion_1_subsection_1_body = factory.fuzzy.FuzzyText(length=10)

    accordion_1_subsection_2_icon = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    accordion_1_subsection_2_heading = factory.fuzzy.FuzzyText(length=10)
    accordion_1_subsection_2_body = factory.fuzzy.FuzzyText(length=10)

    accordion_1_case_study_hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    accordion_1_case_study_button_text = factory.fuzzy.FuzzyText(length=10)
    accordion_1_case_study_button_link = factory.fuzzy.FuzzyText(length=10)
    accordion_1_case_study_title = factory.fuzzy.FuzzyText(length=10)
    accordion_1_case_study_description = factory.fuzzy.FuzzyText(length=10)

    accordion_1_statistic_1_number = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_1_heading = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_1_smallprint = factory.fuzzy.FuzzyText(length=10)

    accordion_1_statistic_2_number = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_2_heading = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_2_smallprint = factory.fuzzy.FuzzyText(length=10)

    accordion_1_statistic_3_number = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_3_heading = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_3_smallprint = factory.fuzzy.FuzzyText(length=10)

    accordion_1_statistic_4_number = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_4_heading = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_4_smallprint = factory.fuzzy.FuzzyText(length=10)

    accordion_1_statistic_5_number = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_5_heading = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_5_smallprint = factory.fuzzy.FuzzyText(length=10)

    accordion_1_statistic_6_number = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_6_heading = factory.fuzzy.FuzzyText(length=10)
    accordion_1_statistic_6_smallprint = factory.fuzzy.FuzzyText(length=10)

    fact_sheet_title = factory.fuzzy.FuzzyText(length=10)
    fact_sheet_teaser = factory.fuzzy.FuzzyText(length=10)
    fact_sheet_column_1_title = factory.fuzzy.FuzzyText(length=10)
    fact_sheet_column_1_teaser = factory.fuzzy.FuzzyText(length=10)
    fact_sheet_column_1_body = factory.fuzzy.FuzzyText(length=10)
    fact_sheet_column_2_title = factory.fuzzy.FuzzyText(length=10)
    fact_sheet_column_2_teaser = factory.fuzzy.FuzzyText(length=10)
    fact_sheet_column_2_body = factory.fuzzy.FuzzyText(length=10)

    help_market_guide_cta_link = factory.fuzzy.FuzzyText(length=10)

    related_page_one = factory.SubFactory(ArticlePageFactory)
    related_page_two = factory.SubFactory(CampaignPageFactory)
    related_page_three = factory.SubFactory(ArticleListingPageFactory)

import factory
import factory.fuzzy
import wagtail_factories
from django.utils import timezone

from export_readiness import models, snippets


class SitePolicyPagesFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.SitePolicyPages

    title = factory.Sequence(lambda n: '123-555-{0}'.format(n))


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


class TagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.Tag

    name = factory.fuzzy.FuzzyText(length=10)


class IndustryTagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.IndustryTag

    name = factory.fuzzy.FuzzyText(length=10)
    icon = factory.SubFactory(wagtail_factories.ImageFactory)


class HomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.HomePage

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


class RegionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.Region

    name = factory.fuzzy.FuzzyText(length=10)


class CountryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = snippets.Country

    name = factory.fuzzy.FuzzyText(length=10)
    slug = factory.fuzzy.FuzzyText(length=10)

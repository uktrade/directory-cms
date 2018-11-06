import factory
import factory.fuzzy
import wagtail_factories
from django.utils import timezone

from export_readiness import models


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


class ArticleListingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.ArticleListingPage

    landing_page_title = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class ArticlePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.ArticlePage

    article_title = factory.fuzzy.FuzzyText(length=10)
    article_teaser = factory.fuzzy.FuzzyText(length=10)
    article_body_text = factory.fuzzy.FuzzyText(length=10)
    related_article_one_url = factory.fuzzy.FuzzyText(length=10)
    related_article_one_title = factory.fuzzy.FuzzyText(length=10)
    related_article_one_teaser = factory.fuzzy.FuzzyText(length=10)
    related_article_two_url = factory.fuzzy.FuzzyText(length=10)
    related_article_two_title = factory.fuzzy.FuzzyText(length=10)
    related_article_two_teaser = factory.fuzzy.FuzzyText(length=10)
    related_article_three_url = factory.fuzzy.FuzzyText(length=10)
    related_article_three_title = factory.fuzzy.FuzzyText(length=10)
    related_article_three_teaser = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


class TagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Tag

    name = factory.fuzzy.FuzzyText(length=10)


class HomePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.HomePage

    news_title = factory.fuzzy.FuzzyText(length=10)
    news_description = factory.fuzzy.FuzzyText(length=10)
    slug = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    last_published_at = timezone.now()
    parent = None


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

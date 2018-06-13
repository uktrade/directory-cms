import factory
import factory.fuzzy
import wagtail_factories

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

    landing_dashboard = False

    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None

import factory
import factory.fuzzy
import wagtail_factories

from directory_constants.constants import choices

from find_a_supplier.models import IndustryPage


class IndustryPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = IndustryPage

    hero_text = factory.fuzzy.FuzzyText(length=255)
    introduction_text = factory.fuzzy.FuzzyText(length=255)
    introduction_column_one_text = factory.fuzzy.FuzzyText(length=255)
    introduction_column_two_text = factory.fuzzy.FuzzyText(length=255)
    introduction_column_three_text = factory.fuzzy.FuzzyText(length=255)
    company_list_text = factory.fuzzy.FuzzyText(length=255)
    company_list_call_to_action_text = factory.fuzzy.FuzzyText(length=255)
    sector_label = factory.fuzzy.FuzzyText(length=255)
    sector_value = factory.fuzzy.FuzzyChoice(
        [i[0] for i in choices.INDUSTRIES]
    )
    seo_description = factory.fuzzy.FuzzyText(length=255)
    title = factory.fuzzy.FuzzyText(length=255)
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None
    introduction_column_two_icon_en_gb = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    introduction_column_three_icon_en_gb = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    introduction_column_one_icon_en_gb = factory.SubFactory(
        wagtail_factories.ImageFactory
    )

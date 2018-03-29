import factory
import factory.fuzzy
import wagtail_factories

from directory_constants.constants import choices

from find_a_supplier import models


class IndustryPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.IndustryPage

    hero_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    introduction_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    introduction_column_one_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    introduction_column_two_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    introduction_column_three_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    company_list_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    company_list_call_to_action_text_en_gb = factory.fuzzy.FuzzyText(
        length=255
    )
    sector_label_en_gb = factory.fuzzy.FuzzyText(length=255)
    sector_value = factory.fuzzy.FuzzyChoice(
        [i[0] for i in choices.INDUSTRIES]
    )
    search_description_en_gb = factory.fuzzy.FuzzyText(length=255)
    title_en_gb = factory.fuzzy.FuzzyText(length=255)
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


class LandingPageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.LandingPage

    hero_text_en_gb = factory.fuzzy.FuzzyText(length=255)
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
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None


class IndustryLandingPagePageFactory(wagtail_factories.PageFactory):

    class Meta:
        model = models.IndustryLandingPage

    hero_title_en_gb = factory.fuzzy.FuzzyText(length=255)
    hero_image = factory.SubFactory(
        wagtail_factories.ImageFactory
    )
    proposition_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    call_to_action_text_en_gb = factory.fuzzy.FuzzyText(length=255)
    breadcrumbs_label_en_gb = factory.fuzzy.FuzzyText(length=255)
    search_description_en_gb = factory.fuzzy.FuzzyText(length=255)
    slug_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    title_en_gb = factory.Sequence(lambda n: '123-555-{0}'.format(n))
    parent = None

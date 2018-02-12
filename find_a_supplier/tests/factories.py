import factory
import factory.fuzzy

from directory_constants.constants import choices

from find_a_supplier.models import CaseStudyPage


class CaseStudyPageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CaseStudyPage

    footer_text = factory.fuzzy.FuzzyText(length=255)
    footer_title = factory.fuzzy.FuzzyText(length=255)
    companies_section_title = factory.fuzzy.FuzzyText(length=255)
    lede = factory.fuzzy.FuzzyText(length=255)
    body = factory.fuzzy.FuzzyText(length=255)
    key_facts = factory.fuzzy.FuzzyText(length=255)
    read_more_text = factory.fuzzy.FuzzyText(length=255)
    layout_class = factory.fuzzy.FuzzyText(length=255)
    seo_description = factory.fuzzy.FuzzyText(length=255)
    sector = factory.fuzzy.FuzzyChoice([i[0] for i in choices.INDUSTRIES])
    depth = 1
    title = factory.fuzzy.FuzzyText(length=255)
    path = '/thing/'
    slug = 'things-things'

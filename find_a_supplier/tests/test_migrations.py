import pytest

from find_a_supplier.tests import factories


@pytest.mark.skip('slow')
@pytest.mark.django_db
def test_populate_breadcrumb(migration, settings):
    page = factories.IndustryContactPageFactory.create(
        breadcrumbs_label_en_gb='breadcrumb [en]',
        breadcrumbs_label_de='breadcrumb [de]',
        breadcrumbs_label_ja='breadcrumb [ja]',
        breadcrumbs_label_ru='breadcrumb [ru]',
        breadcrumbs_label_zh_hans='breadcrumb [zh-hans]',
        breadcrumbs_label_fr='breadcrumb [fr]',
        breadcrumbs_label_es='breadcrumb [es]',
        breadcrumbs_label_pt='breadcrumb [pt]',
        breadcrumbs_label_pt_br='breadcrumb [pt-br]',
        breadcrumbs_label_ar='breadcrumb [ar]',
    )
    migration.before([
        ('core', '0016_auto_20180823_2014'),
    ])

    apps = migration.apply('core', '0017_auto_20180823_1545')
    HistoricBreadcrumb = apps.get_model('core', 'Breadcrumb')
    HistoricContentType = apps.get_model('contenttypes', 'ContentType')
    content_type = HistoricContentType.objects.get_for_model(page)

    breadcrumb = HistoricBreadcrumb.objects.get(
        object_id=page.pk, content_type=content_type
    )

    assert breadcrumb.service_name == page.service_name
    assert breadcrumb.object_id == page.pk
    assert breadcrumb.label_en_gb == 'breadcrumb [en]'
    assert breadcrumb.label_de == 'breadcrumb [de]'
    assert breadcrumb.label_ja == 'breadcrumb [ja]'
    assert breadcrumb.label_ru == 'breadcrumb [ru]'
    assert breadcrumb.label_zh_hans == 'breadcrumb [zh-hans]'
    assert breadcrumb.label_fr == 'breadcrumb [fr]'
    assert breadcrumb.label_es == 'breadcrumb [es]'
    assert breadcrumb.label_pt == 'breadcrumb [pt]'
    assert breadcrumb.label_pt_br == 'breadcrumb [pt-br]'
    assert breadcrumb.label_ar == 'breadcrumb [ar]'

import pytest


from export_readiness.snippets import Tag

@pytest.mark.django_db
def test_tag_str():
    tag = Tag.objects.create(name='Test Tag')
    assert str(tag) == 'Test Tag'

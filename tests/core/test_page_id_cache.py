import pytest

from core.cache import PageIDCache


@pytest.mark.django_db
def test_get_populate_and_delete():

    # the cache should be empty
    assert PageIDCache.get() is None

    # when the page is populated
    result = PageIDCache.populate()

    # then get returns something useful
    assert PageIDCache.get() == result

    # when the cache is cleared
    PageIDCache.clear()

    # then the cache is empty again
    assert PageIDCache.get() is None

    # but we can use populate_if_cold to trigger population
    new_result = PageIDCache.get(populate_if_cold=True)

    # and the result should look very much like what we had before
    assert new_result == result

    # let's clear it again
    PageIDCache.clear()

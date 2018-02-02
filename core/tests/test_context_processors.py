from core import context_processors


def test_feature_flags_installed(settings):
    processors = settings.TEMPLATES[0]['OPTIONS']['context_processors']

    assert 'core.context_processors.feature_flags' in processors


def test_feature_returns_expected_features(settings):
    actual = context_processors.feature_flags(None)

    assert actual == {
        'features': {
        }
    }

from django.conf import settings


def feature_flags(request):
    return {
        'features': {
            'FEATURE_AUTO_TRANSLATE_ENABLED': (
                settings.FEATURE_AUTO_TRANSLATE_ENABLED
            ),
        }
    }

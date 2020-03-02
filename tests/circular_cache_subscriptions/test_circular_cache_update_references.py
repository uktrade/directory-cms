import inspect
from collections import defaultdict

from core.cache import AbstractDatabaseCacheSubscriber
import export_readiness.cache as domestic_cache
import great_international.cache as international_cache


PARENT_MODULE_NAME_DOMESTIC = 'export_readiness.models.'
PARENT_MODULE_NAME_INTERNATIONAL = 'great_international.models.'


def get_list_of_cache_subscriber_classes(cache_module):
    """Gets a list of all cache subscriber classes in a module"""
    return [
        cls for cls
        in cache_module.__dict__.values()
        if inspect.isclass(cls) and issubclass(cls, AbstractDatabaseCacheSubscriber)
    ]


def get_clean_module_class_name_module(cls, parent_module_name):
    key = None
    if hasattr(inspect.getattr_static(cls, 'model'), '__name__'):
        model = inspect.getattr_static(cls, 'model').__name__
        if hasattr(inspect.getmodule(inspect.getattr_static(cls, 'model')), '__name__'):
            module = inspect.getmodule(inspect.getattr_static(cls, 'model')).__name__
            clean_module_name = module.replace(parent_module_name, '')
            key = f"{clean_module_name}.{model}"
    return key


def get_clean_module_class_name_subscription(cls, parent_module_name):
    key = None
    if hasattr(cls, '__name__'):
        subscriber_cls_name = cls.__name__
        if hasattr(inspect.getmodule(cls), '__name__'):
            module = inspect.getmodule(cls).__name__
            clean_module_name = module.replace(parent_module_name, '')
            key = f"{clean_module_name}.{subscriber_cls_name}"
    return key


def get_model_subscriptions(list_of_cache_subscriber_classes, parent_module_name):
    result = defaultdict(list)
    for cls in list_of_cache_subscriber_classes:
        key = get_clean_module_class_name_module(cls, parent_module_name)
        if key:
            if inspect.getattr_static(cls, 'subscriptions'):
                for subscription in inspect.getattr_static(cls, 'subscriptions'):
                    subscription_key = get_clean_module_class_name_subscription(
                        subscription, parent_module_name
                    )
                    if subscription_key:
                        result[key] += [subscription_key]
            else:
                result[key] = []
    return dict(result)


def find_circular_references(cache_subscriptions, ignored_circular_references=None):
    result = []
    for model_class, subscription_classes in cache_subscriptions.items():
        for class_name in subscription_classes:
            if class_name in cache_subscriptions.keys():
                if model_class in cache_subscriptions[class_name]:
                    circular_ref = f"{model_class} in 'model = {class_name}'"
                    if ignored_circular_references:
                        if model_class in ignored_circular_references.keys():
                            if class_name in ignored_circular_references[model_class]:
                                # skip ignored intentional circular reference
                                continue
                            else:
                                result.append(circular_ref)
                    else:
                        result.append(circular_ref)
    return result


def test_circular_cache_update_references_domestic_site():
    subscriber_classes = get_list_of_cache_subscriber_classes(domestic_cache)
    cache_subscriptions = get_model_subscriptions(
        subscriber_classes, PARENT_MODULE_NAME_DOMESTIC
    )
    circular_references = find_circular_references(
        cache_subscriptions
    )

    error = f"Found circular cache update references: {circular_references}"
    assert not circular_references, error


def test_circular_cache_update_references_international_site():
    # ATM There is one circular cache reference defined and commented in
    # /great_international/cache.py
    # Thus, I've added an option to ignore known & expected circular references
    ignored_circular_references = {
        'invest.InvestRegionPage': ['invest.InvestRegionPage']
    }
    subscriber_classes = get_list_of_cache_subscriber_classes(international_cache)
    cache_subscriptions = get_model_subscriptions(
        subscriber_classes, PARENT_MODULE_NAME_INTERNATIONAL
    )
    circular_references = find_circular_references(
        cache_subscriptions, ignored_circular_references
    )

    error = f"Found circular cache update references: {circular_references}"
    assert not circular_references, error

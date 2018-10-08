import abc

from django.core.cache import cache

cache by url and queyrstring as key

on save cache bust:
 - for every language
 - for live and draft


 will not work because related objects will go stale e.g.., breadcrumbs

so breadcrumbs would need seprate cache and

get_many('<url>-<language>-<draft-token>', 'breadcrumbs-<service>')


per model cache bust registry


class AbstractPageCache(abc.ABC):
    # drafts will not be cached
    cache = cache
   
    @property
    @abc.abstractmethod 
    def model(self):
        return

    @property
    @abc.abstractmethod
    def external_change_subscriptions(self):
        return []

    def build_url(self, slug, language_code):
        url = reverse('lookup-by-slug', kwargs={'slug': slug})
        if language_code:
            url += '?lang=' + language_code
        return url

    def save(self, instance):
        url = self.build_url(slug=instance.slug)
        response = request.get(url, {'lang': language_code})
        self.cache.set(cache_key, response.json())
        for language_code in instance.translated_languages:
            url = self.build_url(
                slug=instance.slug, language_code=language_code
            )
            response = request.get(url)
            self.cache.set(url, response.json())

    def bust(self, *args, **kwargs):
        for instance in self.model.objects.all():
            self.save(instance)

    def get(self, slug, language_code=None):
        url = self.build_url(slug=slug, language_code=language_code)
        return self.cache.get(url)

    def subscribe(self):
        for model in self.external_change_subscriptions:
            post_save.connect(
                receiver=self.bust,
                sender=model,
            )

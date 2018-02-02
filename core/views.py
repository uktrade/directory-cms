from django.views.generic import TemplateView


class HelloWorldView(TemplateView):
    template_name = 'core/hello-world.html'

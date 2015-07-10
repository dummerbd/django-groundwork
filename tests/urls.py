"""
urls.py - routes for test project.
"""
from django.conf.urls import include, url
from django.views import TemplateView


class DemoView(TemplateView):
    template_name = 'demo.html'


urlpatterns = [
    url(r'^$', DemoView.as_view())
]

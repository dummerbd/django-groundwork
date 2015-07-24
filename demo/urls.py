"""
urls.py - routes for test project.
"""
from django.conf.urls import url
from django.views.generic import TemplateView


class DemoView(TemplateView):
    template_name = 'groundwork_demo.html'


urlpatterns = [
    url(r'^$', DemoView.as_view())
]

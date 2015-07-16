from django.conf.urls import patterns, url
from django.views.generic import TemplateView


INDEX = 'groundwork/examples/index.html'
ICONS = 'groundwork/examples/icons.html'


# Test patern, renders Zurb Foundation default page using base template
urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=TemplateView.as_view(template_name=INDEX),
        name="groundwork_index"),

    url(regex=r'^icons/$',
        view=TemplateView.as_view(template_name=ICONS),
        name="groundwork_icons"),
)

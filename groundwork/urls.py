from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Test patern, renders Zurb Foundation default page using base template
urlpatterns = patterns('',
    url(regex=r'^$', 
        view=TemplateView.as_view(template_name="groundwork/examples/index.html"), 
        name="groundwork_index"),

    url(regex=r'^icons/$', 
        view=TemplateView.as_view(template_name="groundwork/examples/icons.html"), 
        name="groundwork_icons"),
)

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from groundwork import ICONS


class IconView(TemplateView):
    def get_context_data(self):
        return {'icons': ICONS}


urlpatterns = patterns(
    '',

    url(r'^$',
        TemplateView.as_view(template_name='groundwork/examples/kitchen_sink.html'),
        name="groundwork_index"),

    url(r'^icons/$',
        IconView.as_view(template_name='groundwork/examples/icons.html'),
        name="groundwork_icons"),
)

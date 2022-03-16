from django.views import generic
from django.contrib.auth import get_user_model
from django.http import Http404

User = get_user_model()


class BaseIndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(BaseIndexView, self).get_context_data(**kwargs)

        return context

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class BaseDashboardView(TemplateView):

    template_name = 'dashboard/_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context

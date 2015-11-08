from django.views.generic import TemplateView


class BaseRouteView(TemplateView):

    template_name = 'route/_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context

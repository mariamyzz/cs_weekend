from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views import generic


from .models import Session, Announcement, About, Compendia, Supplementary

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_text'] = About.objects.latest('last_updated_on').text
        return context


class IndexView(TemplateView):
    template_name = "base.html"


class PastSessionsView(generic.ListView):
    model = Session
    template_name = "past.html"
    context_object_name = 'past_sessions'
    paginate_by = 10
    queryset = Session.objects.filter(date__lt=timezone.now()).order_by('-date')


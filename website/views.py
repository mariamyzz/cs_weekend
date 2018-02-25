from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Session, Announcement, About, Compendia, Supplementary

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_text'] = About.objects.latest('last_updated_on').text
        return context


class IndexView(TemplateView):
    template_name = "base.html"


class PastSessionsView(TemplateView):
    template_name = "past.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['past_sessions'] = Session.objects.all()
        return context


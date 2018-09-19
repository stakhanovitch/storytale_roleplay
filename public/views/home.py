# -*- coding: utf-8 -*-
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from public.models.workshop import Workshop
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """
    website homepage with signup capability
    """
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({
            'workshops':self.workshops,
            'title':self.title,
            'meta_description':self.meta_description,
            })
        return context
    title = 'Storytale, Racontez une histoire qui vous ressemble'
    meta_title = title
    meta_description = "Nous organisons des ateliers autour du jeu de rôle à destination des maitres du jeu pour les aider à s'améliorer tout en leur simplifiant la vie"
    workshops = Workshop.objects.filter(start_time__gt=timezone.now())
    template_name = "public/home.html"

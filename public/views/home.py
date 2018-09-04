# -*- coding: utf-8 -*-
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
    title = 'Storytale, Créez des histoires qui vous ressemblent'
    meta_title = title
    meta_description = ""
    workshops = Workshop.objects.all()
    template_name = "public/home.html"

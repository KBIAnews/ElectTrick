# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import LegacyElection
from bakery.views import BuildableListView, BuildableDetailView

# Create your views here.

class LegacyDetailView(BuildableDetailView):
    model = LegacyElection
    template_name = 'elections/legacy_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return LegacyElection.objects.get(slug=self.kwargs['slug'])
        return super(LegacyDetailView, self).get_objects()
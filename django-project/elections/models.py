# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class LegacyElection (models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField("Display Name",
                            max_length=256,
                            help_text="Used internally and on final edited pages.")
    date = models.DateField("Election Date")
    embed_url = models.URLField("Pym Embed URL",
                                help_text="ElectTrick will use pym-loader to generate a seamless page for this election.")
    contained = models.BooleanField("Width Restrictive Container?")

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return "/l/%s/" % self.slug

    class Meta:
        ordering = ['date']
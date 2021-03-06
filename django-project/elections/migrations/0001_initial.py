# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegacyElection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(help_text='Used internally and on final edited pages.', max_length=256, verbose_name='Display Name')),
                ('date', models.DateField(verbose_name='Election Date')),
                ('embed_url', models.URLField(help_text='ElectTrick will use pym-loader to generate a seamless page for this election.', verbose_name='Pym Embed URL')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-19 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0096_auto_20180919_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrierstoparticipation',
            name='systematic_bias',
            field=models.TextField(help_text="<p>Contributing to free and open source software takes some skill. You may have already learned some basic skills through university or college classes, specialized schools, online classes, online resources, or with a mentor, friend, family member or co-worker.</p><p>In these settings, have you faced systematic bias or discrimination? Have you been discouraged from accessing these resources because of your identity or background?</p><p>Please provide specific examples and (optionally) statistics.</p><p>Outreachy Organizers strongly encourage you to write your personal stories. We want you to know that we won't judge your writing style, grammar or spelling.</p>", verbose_name='What systematic bias or discrimination have you faced while building your skills?'),
        ),
    ]

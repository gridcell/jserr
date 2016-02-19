# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JSErrorLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line_number', models.IntegerField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ip', models.IPAddressField(null=True, blank=True)),
                ('browser', models.CharField(max_length=25, null=True, blank=True)),
                ('browser_version', models.CharField(max_length=10, null=True, blank=True)),
                ('os', models.CharField(max_length=25, null=True, blank=True)),
                ('cookies_enabled', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

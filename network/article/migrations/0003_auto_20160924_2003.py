# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_sort_rank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['sort_rank', '-update_time'], 'verbose_name': '\u6559\u7a0b', 'verbose_name_plural': '\u6559\u7a0b'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9'),
        ),
    ]

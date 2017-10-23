# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20171023_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(upload_to=b'static/product_videos/'),
        ),
    ]

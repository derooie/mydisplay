# Generated by Django 2.2 on 2019-07-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0005_line_user_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='display',
            name='font_size',
            field=models.PositiveSmallIntegerField(choices=[(8, 'Small'), (12, 'Normal'), (15, 'Large')], default=12),
        ),
    ]

# Generated by Django 2.2 on 2019-05-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0004_auto_20190504_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='user_text',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]

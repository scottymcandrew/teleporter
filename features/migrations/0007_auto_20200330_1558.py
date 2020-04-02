# Generated by Django 2.2 on 2020-03-30 15:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0006_auto_20200330_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='contributors',
        ),
        migrations.AddField(
            model_name='feature',
            name='funders',
            field=models.ManyToManyField(blank=True, related_name='feature_funders', to=settings.AUTH_USER_MODEL),
        ),
    ]

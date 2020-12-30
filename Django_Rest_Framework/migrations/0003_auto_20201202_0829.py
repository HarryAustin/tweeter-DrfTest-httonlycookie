# Generated by Django 3.0.4 on 2020-12-02 16:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Django_Rest_Framework', '0002_auto_20201202_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetpostdrf',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, through='Django_Rest_Framework.TweetLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
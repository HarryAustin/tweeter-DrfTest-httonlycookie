# Generated by Django 3.0.4 on 2020-11-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xhr_APP', '0002_tweetpost_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetpost',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

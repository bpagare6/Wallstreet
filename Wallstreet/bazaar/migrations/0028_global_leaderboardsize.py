# Generated by Django 2.1.2 on 2019-06-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0027_remove_news_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='global',
            name='LeaderboardSize',
            field=models.IntegerField(default=100),
        ),
    ]

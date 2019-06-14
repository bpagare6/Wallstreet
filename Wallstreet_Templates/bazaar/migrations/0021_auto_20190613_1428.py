# Generated by Django 2.1.2 on 2019-06-13 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0020_auto_20190613_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userhistory',
            old_name='noShares',
            new_name='bidShares',
        ),
        migrations.RenameField(
            model_name='usersharetable',
            old_name='noOfCompanyShares',
            new_name='bidShares',
        ),
        migrations.RenameField(
            model_name='usersharetable',
            old_name='companyOwned',
            new_name='company',
        ),
        migrations.RemoveField(
            model_name='company',
            name='basePointer',
        ),
        migrations.RemoveField(
            model_name='company',
            name='buyEndPointer',
        ),
        migrations.RemoveField(
            model_name='company',
            name='buyStartPointer',
        ),
        migrations.RemoveField(
            model_name='company',
            name='sellEndPointer',
        ),
        migrations.RemoveField(
            model_name='company',
            name='sellStartPointer',
        ),
        migrations.RemoveField(
            model_name='userhistory',
            name='pending',
        ),
    ]
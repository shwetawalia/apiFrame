# Generated by Django 2.2.7 on 2020-04-07 15:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restbasic', '0004_auto_20200407_1446'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Custom_User',
            new_name='Register',
        ),
    ]

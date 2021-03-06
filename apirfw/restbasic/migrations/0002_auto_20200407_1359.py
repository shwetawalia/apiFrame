# Generated by Django 2.2.7 on 2020-04-07 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restbasic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.IntegerField(max_length=10)),
                ('profile_pic', models.ImageField(upload_to='Pics')),
                ('date_of_birth', models.DateField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='programmer',
            name='languages',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Paradigm',
        ),
        migrations.DeleteModel(
            name='Programmer',
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-06 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_org_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='user',
            field=models.ForeignKey(default=None, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
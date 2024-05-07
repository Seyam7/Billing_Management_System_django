# Generated by Django 3.1.7 on 2021-05-19 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyer', '0002_auto_20210516_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyertable',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='buyertable',
            name='address',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
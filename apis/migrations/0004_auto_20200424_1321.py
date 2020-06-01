# Generated by Django 3.0.3 on 2020-04-24 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apis', '0003_auto_20200424_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={},
        ),
        migrations.AlterModelManagers(
            name='driver',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='driver',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2 on 2023-04-29 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='Email_id',
        ),
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

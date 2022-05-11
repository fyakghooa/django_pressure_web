# Generated by Django 4.0.4 on 2022-05-02 14:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressure',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for pressure', primary_key=True, serialize=False),
        ),
    ]

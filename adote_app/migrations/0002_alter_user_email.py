# Generated by Django 5.0.1 on 2024-01-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adote_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=256),
        ),
    ]

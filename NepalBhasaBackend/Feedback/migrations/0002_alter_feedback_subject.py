# Generated by Django 4.0.4 on 2022-07-27 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.TextField(max_length=255),
        ),
    ]

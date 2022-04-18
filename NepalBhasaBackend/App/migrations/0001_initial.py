# Generated by Django 4.0.4 on 2022-04-17 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Lipi',
            fields=[
                ('lipiID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('lipiText', models.ImageField(blank=True, null=True, upload_to='Lipi/')),
                ('category', models.CharField(max_length=255)),
                ('lipiDevnagari', models.CharField(max_length=255)),
                ('lipiEnglish', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'lipi',
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('phraseID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('phraseMeaning', models.CharField(max_length=255)),
                ('phraseDevnagari', models.CharField(max_length=255)),
                ('phraseEnglish', models.CharField(max_length=255)),
                ('phraseLipi', models.ImageField(blank=True, null=True, upload_to='Lipi/')),
                ('phraseNarration', models.FileField(blank=True, upload_to='Narration/')),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
            options={
                'db_table': 'phrase',
            },
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryitem',
            name='definition',
            field=models.CharField(max_length=500),
        ),
    ]

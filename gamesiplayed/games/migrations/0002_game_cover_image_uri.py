# Generated by Django 4.0.3 on 2022-03-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover_image_uri',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]

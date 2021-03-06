# Generated by Django 4.0.4 on 2022-05-12 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spaces', '0007_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlossaryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200)),
                ('definition', models.CharField(blank=True, max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='glossary_item_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='spaces.space')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='glossary_item_updated_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

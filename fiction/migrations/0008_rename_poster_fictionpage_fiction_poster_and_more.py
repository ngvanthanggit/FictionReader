# Generated by Django 5.0.1 on 2024-07-06 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiction', '0007_rename_poster_fiction_poster_homepage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fiction',
            old_name='poster_fictionpage',
            new_name='poster',
        ),
        migrations.RemoveField(
            model_name='fiction',
            name='poster_homepage',
        ),
    ]

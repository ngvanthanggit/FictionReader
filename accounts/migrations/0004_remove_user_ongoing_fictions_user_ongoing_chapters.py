# Generated by Django 5.0.1 on 2024-06-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_favorite_fictions_user_finished_fictions_and_more'),
        ('chapter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ongoing_fictions',
        ),
        migrations.AddField(
            model_name='user',
            name='ongoing_chapters',
            field=models.ManyToManyField(blank=True, related_name='ongoing_fictions', to='chapter.chapter'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-06-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fiction', '0006_alter_fiction_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fictions', models.ManyToManyField(blank=True, to='fiction.fiction')),
            ],
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20200117_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='movie_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='data',
            name='movie',
            field=models.BooleanField(default=False),
        ),
    ]

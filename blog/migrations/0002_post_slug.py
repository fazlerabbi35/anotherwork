# Generated by Django 3.2 on 2021-05-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]

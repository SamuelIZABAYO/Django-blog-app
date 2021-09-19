# Generated by Django 3.2.7 on 2021-09-13 16:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=200, populate_from='title', unique_with=('publish',)),
        ),
    ]
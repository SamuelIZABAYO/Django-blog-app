# Generated by Django 3.2.7 on 2021-09-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0010_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Publish')], default='draft', max_length=10),
        ),
    ]

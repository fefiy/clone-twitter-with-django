# Generated by Django 4.2 on 2023-05-01 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='followed_by',
            new_name='following',
        ),
    ]

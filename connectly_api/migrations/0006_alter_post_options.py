# Generated by Django 5.1.5 on 2025-04-01 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connectly_api', '0005_feed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_view_post', 'Can view post'), ('can_add_post', 'Can add post'), ('can_change_post', 'Can change post'), ('can_delete_post', 'Can delete post')]},
        ),
    ]

# Generated by Django 4.2.5 on 2024-04-10 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_groups', '0003_groupchatroom_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupchatroom',
            name='uid',
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-29 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='email',
        ),
    ]
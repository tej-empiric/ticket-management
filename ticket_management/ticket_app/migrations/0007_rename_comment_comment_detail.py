# Generated by Django 5.0.4 on 2024-04-19 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0006_ticket_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='detail',
        ),
    ]

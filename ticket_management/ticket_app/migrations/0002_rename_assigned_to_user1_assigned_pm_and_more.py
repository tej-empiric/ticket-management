# Generated by Django 5.0.4 on 2024-04-11 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user1',
            old_name='assigned_to',
            new_name='assigned_PM',
        ),
        migrations.AddField(
            model_name='user1',
            name='assigned_TL',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

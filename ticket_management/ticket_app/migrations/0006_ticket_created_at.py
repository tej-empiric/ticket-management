# Generated by Django 5.0.4 on 2024-04-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0005_alter_ticket_created_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
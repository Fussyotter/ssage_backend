# Generated by Django 4.1.7 on 2023-04-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssage_api', '0007_message_is_seen_conversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]

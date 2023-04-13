# Generated by Django 4.1.7 on 2023-04-13 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssage_api', '0009_delete_conversation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GiftName', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('Price', models.CharField(max_length=255)),
                ('Link', models.URLField(max_length=255)),
                ('AlternativeLink', models.URLField(max_length=255)),
            ],
        ),
    ]
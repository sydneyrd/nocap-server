# Generated by Django 4.1.6 on 2023-04-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nocapapi', '0013_sharedcharactertoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculatedroster',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

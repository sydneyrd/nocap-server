# Generated by Django 4.1.6 on 2023-04-04 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nocapapi', '0011_alter_charlink_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculatedroster',
            name='is_public',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='charlink',
            name='calculated_roster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calculated_roster_links', to='nocapapi.calculatedroster'),
        ),
    ]

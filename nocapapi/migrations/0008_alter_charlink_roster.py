# Generated by Django 4.1 on 2022-10-06 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nocapapi', '0007_alter_charlink_roster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charlink',
            name='roster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link_roster', to='nocapapi.calculatedroster'),
        ),
    ]

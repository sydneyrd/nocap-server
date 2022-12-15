# Generated by Django 4.1 on 2022-11-09 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nocapapi', '0004_character_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500, verbose_name='link')),
                ('calculated_roster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calculated_roster', to='nocapapi.calculatedroster')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character', to='nocapapi.character')),
            ],
        ),
    ]

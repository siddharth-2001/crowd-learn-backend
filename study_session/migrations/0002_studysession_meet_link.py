# Generated by Django 4.1.1 on 2022-09-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studysession',
            name='meet_link',
            field=models.URLField(default=''),
        ),
    ]

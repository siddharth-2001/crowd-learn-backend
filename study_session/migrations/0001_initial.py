# Generated by Django 4.1.1 on 2022-09-24 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
        ('learner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudySession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('details', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='learner.learner')),
                ('teacher', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]

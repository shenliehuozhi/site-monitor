# Generated by Django 2.0.5 on 2018-05-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('frequency', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('master_schedule_id', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('stoped', 'stoped'), ('running', 'running')], default='stoped', max_length=20)),
                ('tasks', models.TextField(default='[]')),
                ('resutls', models.TextField(default='[]')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-10 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0044_task_post_time_usertask_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWeeklyChallenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start_date', models.DateField()),
                ('challenge_text', models.CharField(default='8-часовой сон', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_challenges', to='game.users')),
            ],
            options={
                'unique_together': {('user', 'week_start_date')},
            },
        ),
    ]

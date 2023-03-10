# Generated by Django 4.1.4 on 2022-12-27 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showtimes', '0001_initial'),
        ('theaters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTheaterTicket',
            fields=[
                ('theater_ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('movie_showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showtimes.movieshowtime')),
                ('movie_theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theaters.movietheater')),
            ],
            options={
                'db_table': 'movie_theater_tickets',
            },
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-28 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(max_length=150)),
                ('reps', models.PositiveSmallIntegerField(default=0)),
                ('sets', models.PositiveSmallIntegerField(default=0)),
                ('distance', models.DecimalField(decimal_places=6, max_digits=9)),
                ('time', models.DecimalField(decimal_places=6, max_digits=9)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]

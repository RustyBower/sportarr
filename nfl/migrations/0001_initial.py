# Generated by Django 2.1 on 2019-09-04 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("path", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("short_name", models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Week",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("season", models.IntegerField()),
                ("week", models.IntegerField()),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("PRE", "Preseason"),
                            ("REG", "Regular Season"),
                            ("POST", "Postseason"),
                        ],
                        max_length=4,
                    ),
                ),
                ("date", models.DateTimeField(verbose_name="date")),
                (
                    "away",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="away",
                        to="nfl.Team",
                    ),
                ),
                (
                    "file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="file",
                        to="nfl.File",
                    ),
                ),
                (
                    "home",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home",
                        to="nfl.Team",
                    ),
                ),
            ],
        ),
    ]

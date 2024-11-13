# Generated by Django 5.1.3 on 2024-11-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "budget",
                    models.DecimalField(decimal_places=2, default=0, max_digits=15),
                ),
                ("homepage", models.CharField(blank=True, max_length=100)),
                ("original_language", models.CharField(max_length=10)),
                ("original_title", models.CharField(max_length=100)),
                ("overview", models.TextField(blank=True)),
                ("release_date", models.DateField(blank=True, null=True)),
                (
                    "revenue",
                    models.DecimalField(decimal_places=2, default=0, max_digits=15),
                ),
                ("runtime", models.IntegerField(default=0)),
                ("status", models.CharField(blank=True, max_length=50)),
                (
                    "vote_average",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("vote_count", models.IntegerField(default=0)),
                ("production_company_id", models.IntegerField(default=0)),
                ("genre_id", models.IntegerField(default=0)),
                ("languages", models.CharField(max_length=100)),
            ],
        ),
    ]

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    homepage = models.CharField(max_length=100, blank=True)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    runtime = models.IntegerField(default=0)
    status = models.CharField(max_length=50, blank=True)
    vote_average = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    vote_count = models.IntegerField(default=0)
    production_company_id = models.IntegerField(default=0)
    genre_id = models.IntegerField(default=0)
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.title

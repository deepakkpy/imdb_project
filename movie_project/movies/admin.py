from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'original_language', 'vote_average', 'status')  # Fields to display
    search_fields = ('title', 'original_language', 'status')  # Fields to search by
    list_filter = ('release_date', 'original_language', 'status')  # Filters on the right side of the list
    ordering = ('-release_date',)  # Default ordering by release_date descending


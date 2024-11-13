from datetime import datetime
from decimal import Decimal
from django.core.paginator import Paginator
from django.db.models import QuerySet

MAX_TITLE_LENGTH = 100  # Define max length constants

class DataParser:
    @staticmethod
    def truncate_to_max_length(value, max_length=MAX_TITLE_LENGTH):
        """Truncate string to max length."""
        return value[:max_length] if value else value

    @staticmethod
    def parse_decimal(value):
        """Parse string to Decimal, with error handling."""
        try:
            return Decimal(value) if value else Decimal(0)
        except (ValueError, TypeError):
            return Decimal(0)

    @staticmethod
    def parse_date(date_string):
        """Parse string to date (YYYY-MM-DD) format."""
        if not date_string:
            return None
        try:
            return datetime.strptime(date_string, '%Y-%m-%d').date()
        except ValueError:
            return None

class MovieQueryService:
    @staticmethod
    def filter_movies(queryset: QuerySet, release_year: str = None, language: str = None):
        """Apply filters to the Movie queryset."""
        if release_year:
            queryset = queryset.filter(release_date__year=release_year)
        if language:
            queryset = queryset.filter(original_language=language)
        return queryset

    @staticmethod
    def sort_movies(queryset: QuerySet, sort_by: str = None):
        """Apply sorting to the Movie queryset."""
        if sort_by == 'release_date':
            return queryset.order_by('release_date')
        elif sort_by == 'ratings':
            return queryset.order_by('-vote_average')
        return queryset

class PaginatorService:
    @staticmethod
    def paginate(queryset: QuerySet, page_number: int = 1, page_size: int = 10):
        """Paginate the queryset and return a page object."""
        paginator = Paginator(queryset, page_size)
        return paginator.get_page(page_number)

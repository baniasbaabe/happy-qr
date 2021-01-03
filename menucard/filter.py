import django_filters
from menucard.models import *
from django_filters import DateFilter


class BesucherFilter(django_filters.FilterSet):
    start_datum = DateFilter(field_name='besucht_am', lookup_expr='gte', label='Anfangsdatum')
    end_datum = DateFilter(field_name='besucht_am', lookup_expr='lte', label='Enddatum ')

    class Meta:
        model = Besucher
        fields = '__all__'
        exclude = ['kundeId', 'besucht_am', 'telefon', 'strasse', 'hausnummer']

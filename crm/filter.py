import django_filters
from crm.models import *
from django_filters import DateFilter


class KundenFilter(django_filters.FilterSet):
    class Meta:
        model = Kunde
        fields = [
            'vorname',
            'nachname',
            'email',
            'telefon',
        ]


class MitarbeiterFilter(django_filters.FilterSet):
    class Meta:
        model = Mitarbeiter
        fields = [
            'vorname',
            'nachname',
            'email',
            'telefon',
        ]


class AuftragsFilter(django_filters.FilterSet):
    start_datum = DateFilter(field_name='auftrag_vom', lookup_expr='gte', label='Anfangsdatum')
    end_datum = DateFilter(field_name='auftrag_vom', lookup_expr='lte', label='Enddatum')

    class Meta:
        model = Auftrag
        fields = [
            'kunde',
            'status',
        ]


class RechnungenFilter(django_filters.FilterSet):
    start_datum = DateFilter(field_name='datum', lookup_expr='gte', label='Anfangsdatum')
    end_datum = DateFilter(field_name='datum', lookup_expr='lte', label='Enddatum ')

    class Meta:
        model = Rechnung
        fields = [
            'kunde',
        ]

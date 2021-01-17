import django_filters
from menucard.models import *
from django_filters import DateFilter


class BesucherFilter(django_filters.FilterSet):
    """
            Eine Klasse zur Repräsentation eines Besucherfilters

            ...

            Attributes
             ----------
            start_datum : datefilter
                Startdatum des Filters
            enddatum : datefilter
                Enddatum des Filters

            Classes
            ----------
            Meta:
                Felderdefinitionen der Form

    """
    start_datum = DateFilter(field_name='besucht_am', lookup_expr='gte', label='Anfangsdatum')
    end_datum = DateFilter(field_name='besucht_am', lookup_expr='lte', label='Enddatum ')

    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Besucher
                    Besucherobjekt
                fields : string
                    Felder des Besuchers
                excludes : list
                    Die Felder, die nicht im Filter enthalten sein sollen



        """
        model = Besucher
        fields = '__all__'
        exclude = ['kundeId', 'besucht_am', 'telefon', 'strasse', 'hausnummer']

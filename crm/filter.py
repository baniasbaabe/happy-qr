import django_filters
from crm.models import *
from django_filters import DateFilter


class KundenFilter(django_filters.FilterSet):
    """
            Eine Klasse zur Repräsentation eines Kundenfilters

            ...

            Classes
            ----------
            Meta:
                Felderdefinitionen der Form

    """
    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Kunde
                    Kundenobjekt
                fields : list
                    Felder des Kunden



        """
        model = Kunde
        fields = [
            'vorname',
            'nachname',
            'email',
            'telefon',
        ]


class MitarbeiterFilter(django_filters.FilterSet):
    """
            Eine Klasse zur Repräsentation eines Mitarbeiterfilters

            ...

            Classes
            ----------
            Meta:
                Felderdefinitionen der Form

    """
    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Mitarbeiter
                    Mitarbeiterobjekt
                fields : list
                    Felder des Mitarbeiters



        """
        model = Mitarbeiter
        fields = [
            'vorname',
            'nachname',
            'email',
            'telefon',
        ]


class AuftragsFilter(django_filters.FilterSet):
    """
            Eine Klasse zur Repräsentation eines Auftragfilters

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
    start_datum = DateFilter(field_name='auftrag_vom', lookup_expr='gte', label='Anfangsdatum')
    end_datum = DateFilter(field_name='auftrag_vom', lookup_expr='lte', label='Enddatum')

    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Auftrag
                    Auftragsobjekt
                fields : list
                    Felder des Auftrags



        """
        model = Auftrag
        fields = [
            'kunde',
            'status',
        ]


class RechnungenFilter(django_filters.FilterSet):
    """
            Eine Klasse zur Repräsentation eines Rechnungfilters

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
    start_datum = DateFilter(field_name='datum', lookup_expr='gte', label='Anfangsdatum')
    end_datum = DateFilter(field_name='datum', lookup_expr='lte', label='Enddatum ')

    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Rechnung
                    Rechnungsobjekt
                fields : list
                    Felder der Rechnung



        """
        model = Rechnung
        fields = [
            'kunde',
        ]

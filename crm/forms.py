from django.forms import ModelForm
from .models import *


class KundeForm(ModelForm):
    class Meta:
        model = Kunde
        fields = '__all__'


class MitarbeiterForm(ModelForm):
    class Meta:
        model = Mitarbeiter
        fields = '__all__'

class AuftragForm(ModelForm):
    class Meta:
        model = Auftrag
        fields = "__all__"


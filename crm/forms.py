from django.forms import ModelForm
from .models import *

class KundeForm(ModelForm):
    class Meta:
        model = Kunde
        fields = '__all__'

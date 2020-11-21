from django.contrib import admin

# Register your models here.
from crm.models import *

admin.site.register(Mitarbeiter)
admin.site.register(Kunde)
admin.site.register(Auftrag)
admin.site.register(Rechnung)

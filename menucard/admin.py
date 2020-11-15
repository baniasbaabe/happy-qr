from django.contrib import admin

# Register your models here.
from menucard.models import *

admin.site.register(Vorspeise)
admin.site.register(Hauptspeise)
admin.site.register(Nachspeise)
admin.site.register(Snacks)
admin.site.register(AlkoholfreieDrinks)
admin.site.register(AlkoholhaltigeDrinks)

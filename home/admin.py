from django.contrib import admin
from .models import Confeiteiro, Bolo

class detBolo(admin.ModelAdmin):
    list_display = (
        'id', 
        'sabor', 
        'descricao', 
        'confeiteiro', 
        'data_fabricacao', 
        'data_validade', 
        'foto',
        'mostrar'
    )
    list_display_links = ('sabor', )
    search_fields = ('sabor', )

admin.site.register(Confeiteiro)
admin.site.register(Bolo, detBolo)

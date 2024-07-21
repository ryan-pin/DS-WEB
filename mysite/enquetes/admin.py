from django.contrib import admin

from .models import Pergunta, Alternativa
'''
class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 3

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['texto_perg']})
        ('Informações de data:', {'fields':['data_pub']}),
    ]
    inlines = [AlternativaInline]
    list_display = ('texto_perg', 'id', 'data_pub')
'''
admin.site.register(Pergunta)
admin.site.register(Alternativa)

# Register your models here.

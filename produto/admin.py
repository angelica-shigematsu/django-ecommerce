from django.contrib import admin
from . import models
# Register your models here.

class VariacaoInline(admin.TabularInline):
  model = models.Varicao
  extra = 1

class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'descricao_curta', 'get_preco_formatado', 'preco_marketing_promocional']
  inlines = [
    VariacaoInline
  ]

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Varicao)

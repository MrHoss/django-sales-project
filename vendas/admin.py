# vendas/admin.py
from django.contrib import admin
from .models import Venda
from itens_venda.models import ItemVenda

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1  # Número de formulários em branco a serem exibidos

class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'vendedor', 'data_venda', 'total')
    inlines = [ItemVendaInline]

admin.site.register(Venda, VendaAdmin)

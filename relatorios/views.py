from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from io import BytesIO
import pandas as pd
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .serializers import VendaSerializer
from vendas.models import Venda
from itens_venda.models import ItemVenda

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from io import BytesIO
import pandas as pd
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .serializers import VendaSerializer
from vendas.models import Venda
from itens_venda.models import ItemVenda

class RelatorioViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def vendas(self, request):
        data_inicial = request.query_params.get('data_inicial')
        data_final = request.query_params.get('data_final')
        vendedor = request.query_params.get('vendedor')
        cliente = request.query_params.get('cliente')
        formato = request.query_params.get('formato', 'pdf')

        queryset = Venda.objects.all()
        if data_inicial and data_final:
            queryset = queryset.filter(data_venda__range=[data_inicial, data_final])
        if vendedor:
            queryset = queryset.filter(vendedor__nome__icontains=vendedor)
        if cliente:
            queryset = queryset.filter(cliente__nome__icontains=cliente)

        if formato == 'excel':
            return self.export_to_excel(queryset)
        else:
            return self.export_to_pdf(queryset)



    def export_to_excel(self, queryset):
        vendas = []
        for venda in queryset:
            itens = venda.itens.all().values('produto__nome', 'produto__preco', 'quantidade')
            for item in itens:
                vendas.append({
                    'venda_id': venda.id,
                    'data_venda': venda.data_venda,
                    'cliente': venda.cliente.nome,
                    'vendedor': venda.vendedor.nome,
                    'produto': item['produto__nome'],
                    'preco': item['produto__preco'],
                    'quantidade': item['quantidade'],
                    'total': item['produto__preco'] * item['quantidade'],
                })
    
        df = pd.DataFrame(vendas)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Vendas', index=False)
        output.seek(0)
        response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="vendas.xlsx"'
        return response

    def export_to_pdf(self, queryset):
        template_path = 'relatorios/vendas_pdf.html'
        vendas = []
        for venda in queryset:
            itens = venda.itens.all()
            vendas.append({
                'venda': venda,
                'itens': itens
            })
        
        context = {'vendas': vendas}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="vendas.pdf"'
        
        template = get_template(template_path)
        html = template.render(context)
        
        # Use BytesIO to handle the content
        result = BytesIO()
        pisa_status = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=result)
        result.seek(0)
        
        response.write(result.read())
        
        return response if not pisa_status.err else HttpResponse('Error Rendering PDF', status=500)


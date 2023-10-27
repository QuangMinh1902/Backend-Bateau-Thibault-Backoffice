from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct, TransactionModel
from monTiGMagasin.serializers import InfoProductSerializer, PutOnSaleSerializer, TransactionSerializer

# Create your views here.
class InfoProductList(APIView):
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)
class InfoProductDetail(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
    
class PutOnSale(APIView):
    def get(self,request, tig_id, new_price, format=None):
        try:
            product = InfoProduct.objects.get(id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
        
        new_price_float = float(new_price)
        product.sale = True
        product.discount = new_price_float
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
class RemoveSale(APIView):
    def get(self,request, tig_id, format=None):
        try:
            product = InfoProduct.objects.get(id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
        
        
        product.sale = False
        product.discount = 0.0
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
    
class IncrementStock(APIView):
    def get(self,request, tig_id, number , format=None):
        try:
            product = InfoProduct.objects.get(id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
        
        print(product)
        product.quantityInStock += number
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
    
class DecrementStock(APIView):
    def get(self,request, tig_id, number , format=None):
        try:
            product = InfoProduct.objects.get(id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
        
        
        product.quantityInStock -= number
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
class Transaction(APIView):
    def get(self, request, format=None):
        products = TransactionModel.objects.all()
        #print("Hello" + products)
        serializer = TransactionSerializer(products, many=True)
        return Response(serializer.data)
    
    
class TransactionsByMonth(APIView):
    
    def get(self, request, month_id, format=None):
        # Filtrer les transactions par mois_id
        month_transactions = TransactionModel.objects.filter(selling_date__month=month_id)
        serializer = TransactionSerializer(month_transactions, many=True)
        return Response(serializer.data)
    
    

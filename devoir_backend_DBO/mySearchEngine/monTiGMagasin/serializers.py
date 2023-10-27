from rest_framework.serializers import ModelSerializer
from monTiGMagasin.models import InfoProduct, TransactionModel


class InfoProductSerializer(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('id', 'tig_id', 'name', 'category', 'price', 'unit', 'availability', 'sale', 'discount', 'comments', 'owner', 'quantityInStock')


class PutOnSaleSerializer(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('id', 'tig_id', 'name', 'category', 'price', 'unit', 'availability', 'sale', 'discount', 'comments', 'owner', 'quantityInStock')

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = '__all__'
        
        
        
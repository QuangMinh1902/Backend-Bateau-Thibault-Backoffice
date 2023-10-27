from django.db import models

# Create your models here.
class InfoProduct(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tig_id = models.IntegerField(default='-1')
    name = models.CharField(max_length=100, blank=True, default='')
    category = models.IntegerField(default='-1')
    price = models.FloatField(default='0')
    unit = models.CharField(max_length=20, blank=True, default='')
    availability = models.BooleanField(default=True)
    sale = models.BooleanField(default=False)
    discount = models.FloatField(default='0')
    comments = models.CharField(max_length=100, blank=True, default='')
    owner = models.CharField(max_length=20, blank=True, default='tig_orig')
    quantityInStock = models.IntegerField(default='0')

    class Meta:
        ordering = ('name',)
        


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name="Name of product", unique=True)
    category = models.IntegerField(default=5, verbose_name="Category", blank=False, null=False)
    unit = models.CharField(max_length=20, verbose_name="Unit")
    price = models.FloatField(default=0, verbose_name="Price")
    price_selling = models.FloatField(default=0, verbose_name="Price selling")
    price_on_sale = models.FloatField(default=0, verbose_name="Price on sale", blank=False, null=False)
    number_prod_sold = models.IntegerField(default=0, verbose_name="Number of product sold", blank=False, null=False)
    availability = models.BooleanField(default=True, verbose_name="Availability")
    sale = models.BooleanField(default=False, verbose_name="Sale")
    discount = models.FloatField(default=0, verbose_name="Discount")
    comments = models.TextField(verbose_name="Comment", blank=True, null=True)
    owner = models.CharField(max_length=20, verbose_name="Name of owner", blank=False, null=False)
    quantity_in_stock = models.IntegerField(default=50, verbose_name="Stock quantity", blank=False, null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.price:
            self.price_selling = self.price + 5.0
        super(Product, self).save(*args, **kwargs)



      
class TransactionModel(models.Model):
    id_product = models.IntegerField()
    selling_date = models.DateTimeField(auto_now_add=True)
    selling_quantity = models.IntegerField()
    amount_total = models.FloatField(default=0.0)
    category = models.IntegerField(default=-1)

    class Meta:
        ordering = ('id_product',)
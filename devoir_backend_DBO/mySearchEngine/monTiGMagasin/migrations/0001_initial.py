# Generated by Django 4.2.6 on 2023-10-25 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tig_id', models.IntegerField(default='-1')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('category', models.IntegerField(default='-1')),
                ('price', models.FloatField(default='0')),
                ('unit', models.CharField(blank=True, default='', max_length=20)),
                ('availability', models.BooleanField(default=True)),
                ('sale', models.BooleanField(default=False)),
                ('discount', models.FloatField(default='0')),
                ('comments', models.CharField(blank=True, default='', max_length=100)),
                ('owner', models.CharField(blank=True, default='tig_orig', max_length=20)),
                ('quantityInStock', models.IntegerField(default='0')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name of product')),
                ('category', models.IntegerField(default=5, verbose_name='Category')),
                ('unit', models.CharField(max_length=20, verbose_name='Unit')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('price_selling', models.FloatField(default=0, verbose_name='Price selling')),
                ('price_on_sale', models.FloatField(default=0, verbose_name='Price on sale')),
                ('number_prod_sold', models.IntegerField(default=0, verbose_name='Number of product sold')),
                ('availability', models.BooleanField(default=True, verbose_name='Availability')),
                ('sale', models.BooleanField(default=False, verbose_name='Sale')),
                ('discount', models.FloatField(default=0, verbose_name='Discount')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('owner', models.CharField(max_length=20, verbose_name='Name of owner')),
                ('quantity_in_stock', models.IntegerField(default=50, verbose_name='Stock quantity')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selling_date', models.DateTimeField(auto_now_add=True)),
                ('id_product', models.IntegerField(default=-1)),
                ('amount_total', models.FloatField(default=0.0)),
                ('selling_quantity', models.IntegerField(default=-1)),
                ('category', models.IntegerField(default=-1)),
            ],
            options={
                'ordering': ('id_product',),
            },
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-27 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('suser', '0001_initial'),
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shop_deliveries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveries.shopdelivery')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.shopproduct')),
                ('shop_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suser.shopsuser')),
            ],
            options={
                'db_table': 'shop_orders',
            },
        ),
    ]

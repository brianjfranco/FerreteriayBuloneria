# Generated by Django 5.0.4 on 2024-09-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0005_alter_detallefactura_precio_unitario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='numero_comprobante',
            field=models.CharField(max_length=13, unique=True, verbose_name='Número de Comprobante'),
        ),
    ]
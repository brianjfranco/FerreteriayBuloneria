# Generated by Django 4.2.15 on 2024-09-01 03:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=50)),
                ('direccion', models.CharField(blank=True, default='', max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MedioDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('EF', 'Efectivo'), ('TC', 'Tarjeta de Crédito'), ('TD', 'Tarjeta de Débito'), ('TR', 'Transferencia Bancaria')], max_length=2, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='contacto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='fecha_hora',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tipo_producto',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='venta',
            name='detalle_ventas',
            field=models.ManyToManyField(through='miAplicacion.DetalleVenta', to='miAplicacion.producto'),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='venta',
            name='importe_total',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=10),
        ),
        migrations.AddField(
            model_name='venta',
            name='numero_comprobante',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidad',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.producto'),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.venta'),
        ),
        migrations.AlterField(
            model_name='movimientostock',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad_stock',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10,default=0.00)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='miAplicacion.factura')),
                ('medio_de_pago', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.mediodepago')),
                ('producto', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='miAplicacion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='medio_de_pago',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.mediodepago'),
        ),
    ]
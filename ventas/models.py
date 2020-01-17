from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from inventario.models import Productos,Tallas
from seguridad.models import Cliente
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

class Carrito_Compras(models.Model):
	session=models.CharField(max_length=18,null=False)
	id_producto=models.ForeignKey(Productos,on_delete=models.PROTECT)
	cantidad=models.IntegerField(null=False)
	talla=models.ForeignKey(Tallas,on_delete=models.PROTECT)
	
	def __str__(self):
		return self.session
	
class Estatus_Venta(models.Model):
	estatus_venta=models.CharField(max_length=30,null=False)
	
	def __str__(self):
		return self.estatus_venta

#indica el canal de venta, Facebook, Mercado Libre, Instagram etc.
class Medio_Venta(models.Model):
	desc_medio=models.CharField(max_length=30)

	def __str__(self):
		return self.desc_medio

class Venta(models.Model):
	fecha=models.DateTimeField(default=timezone.now())
	costo_envio=models.DecimalField(max_digits=20,decimal_places=2,default=0.00)
	sub_total=models.DecimalField(max_digits=20,decimal_places=2,null=False)
	descuento=models.DecimalField(max_digits=20,decimal_places=2,null=True,default=0)
	iva=models.DecimalField(max_digits=20,decimal_places=2,null=False)	
	total=models.DecimalField(max_digits=20,decimal_places=2,null=False)
	id_estatus_venta=models.ForeignKey(Estatus_Venta,on_delete=models.PROTECT,default=1)
	link_seguimiento=models.CharField(max_length=200,null=True,default='No Disponible')
	cliente=models.ForeignKey(Cliente,on_delete=models.PROTECT,null=True)
	id_medio_venta=models.ForeignKey(Medio_Venta,on_delete=models.PROTECT,null=True)

class Detalle_Venta(models.Model):
	id_venta=models.ForeignKey(Venta,on_delete=models.PROTECT)
	id_producto=models.ForeignKey(Productos,on_delete=models.PROTECT,null=True)	
	talla=models.ForeignKey(Tallas,on_delete=models.PROTECT,null=True)
	#talla=ChainedForeignKey(Tallas,chained_field="id_producto",
    #    chained_model_field="id_producto",
    #    show_all=False,
    #    auto_choose=True,
    #    sort=True)
	cantidad=models.IntegerField(null=False,default=0)
	precio_unitario=models.DecimalField(max_digits=20,decimal_places=2,null=False,default=0.00)#almacena el precio antes de descuento e impuesto
	descuento=models.DecimalField(max_digits=20,decimal_places=2,null=True,default=0.00)#almacena el importe de descuento
	iva=models.DecimalField(max_digits=20,decimal_places=2,null=True,default=0.00)#almacena el iva
	precio_total=models.DecimalField(max_digits=20,decimal_places=2,null=False,default=0.00)#almacena el precio de todos los productos (precio_unitario*cantidad)
	
class Direccion_Envio_Venta(models.Model):
	id_venta=models.ForeignKey(Venta,on_delete=models.PROTECT)
	nombre_recibe=models.CharField(max_length=20,null=False)
	apellido_p=models.CharField(max_length=20,null=False)
	apellido_m=models.CharField(max_length=20,null=True)
	calle=models.CharField(max_length=50,null=False)
	numero_interior=models.CharField(max_length=10,null=True)	
	numero_exterior=models.CharField(max_length=10,null=True)	
	cp=models.CharField(max_length=10,null=False)
	colonia=models.CharField(max_length=50,null=True)	
	municipio=models.CharField(max_length=50,null=False,default="")
	estado=models.CharField(max_length=50,null=False,default="")
	pais=models.CharField(max_length=50,null=False,default="")
	telefono=models.CharField(max_length=20,null=False)
	correo_electronico=models.CharField(max_length=50,null=False)
	referencia=models.CharField(max_length=200,null=False)
	
	
from django.conf.urls import include,url
from .views import api_cont_productos_carrito,api_crea_venta,api_consulta_carrito_compras,api_elimina_carrito_compras,registro_medio_venta,api_genera_cupon,api_libera_carrito,api_reinicia_tiempo_carrito

from ventas import views

app_name="ventas"
urlpatterns=[
	#formularios
	url(r'^busca_ventas/$',views.busca_ventas,name="busca_ventas"),
	url(r'^detalle_venta/(?P<id_venta>\d+)/$',views.detalle_venta_form,name="detalle_venta"),
	url(r'^reenvia_mail/(?P<id_venta>\d+)/$',views.reenvia_venta,name="reenvia_mail"),
	url(r'^guarda_venta_manual/$',views.guarda_venta_manual,name="guarda_venta_manual"),	
	
	url(r'^registro_medio_venta/$',views.registro_medio_venta,name="registro_medio_venta"),	
	
	#apis
	url(r'^carrito_compras/$',api_consulta_carrito_compras),	
	url(r'^elimina_prod_carrito/$',api_elimina_carrito_compras),
	url(r'^libera_carrito/$',api_libera_carrito),
	url(r'^reinicia_tiempo_carrito/$',api_reinicia_tiempo_carrito),
	
	url(r'^cont_prod_carrito/$',api_cont_productos_carrito),		
	url(r'^guarda_venta/$',api_crea_venta),		
	url(r'^conslta_ventas_cliente/$',views.api_consulta_ventas),		
	url(r'^consulta_detalle_venta/$',views.api_consulta_detalle_venta),		
	url(r'^genera_cargo/$',views.api_genera_cargo),		
	url(r'^genera_cupon/$',views.api_genera_cupon),	
	
		

	
	
	

	
]



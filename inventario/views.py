from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Productos,Atributos,Tallas,Img_Producto,Estatus,Productos_Relacionados,Municipio,Estado,Pais
from .models import Rel_Producto_Categoria,Categorias,Proveedor,Productos_Temp
from django.http import QueryDict
from django.db.models import Sum
from .forms import Productos_Form,Proveedores_Form,Busqueda_Producto_Form,Busca_Proveedores_Form,Consulta_Existencia_Form
from .forms import Categorias_Form,Busca_X_Clave_Prod_Prov_Form
import decimal
from django.forms.models import inlineformset_factory
from django.template import RequestContext as ctx
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.db.models import Max


def consulta_stock(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('seguridad:login'))


	if request.method=="POST":
		reporte=[]
		txt_palabra=request.POST.get("producto")
		id_producto=request.POST.get("id_producto")
		clave_proveedor=request.POST.get("clave_proveedor")
		if id_producto=="":
			id_producto=0

		if id_producto!=0:
			producto=Productos.objects.filter(id=id_producto)
		else:
			#si se requiere buscar por todos los parametros.
			if txt_palabra!=""  and clave_proveedor!="":
				producto=Productos.objects.filter(desc_producto__icontains=txt_palabra,clave_prod_proveedor__icontains=clave_proveedor)
			else:
				if txt_palabra!="":
					producto=Productos.objects.filter(desc_producto__icontains=txt_palabra)					
				else:
					producto=Productos.objects.filter(clave_prod_proveedor__icontains=clave_proveedor)					

		#es en las tallas donde tenemos el stock			
		t=Tallas.objects.filter(id_producto__in=producto)
		for x in t:			
			reporte.append({"talla":x.talla,"id":x.id_producto.id,"nombre":str(x.id_producto.id)+' - '+x.id_producto.nombre,"marca":x.id_producto.marca,"clave_proveedor":x.id_producto.clave_prod_proveedor,"entrada":x.entrada,"salida":x.salida,"apartado":x.apartado,"existencia":(x.entrada+x.apartado-x.salida)})	

		form=Consulta_Existencia_Form(request.POST)
	else:
		print("no hay nada")
		form=Consulta_Existencia_Form()
	return render(request,'inventario/consulta_stock.html',locals())

#formulario de busqueda de producto
def busca_producto(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('seguridad:login'))

	if request.method=="POST":

		if request.POST.get("id_proveedor")=='':
			proveedor=0
		else:
			proveedor=int(request.POST.get("id_proveedor"))

		if request.POST.get("id_estatus")=='':
			estatus=0
		else:
			estatus=int(request.POST.get("id_estatus"))

		if request.POST.get("id_producto")=='':
			id_producto=0
		else:
			id_producto=int(request.POST.get("id_producto"))

		if request.POST.get("clave_proveedor")=='NA':
			cve_prod_proveedor="0"
		else:
			cve_prod_proveedor=request.POST.get("clave_proveedor")

		pml=request.POST.get("pml")

		if cve_prod_proveedor!="0":
			producto=Productos.objects.filter(clave_prod_proveedor=cve_prod_proveedor).order_by("id")
		else:
			if proveedor==0 and estatus==0 and id_producto==0:
				producto=Productos.objects.all().order_by("id")

			if id_producto>0:
				producto=Productos.objects.filter(id=id_producto).order_by("id")
			else:
				if proveedor>0 and estatus==0:
					if pml=="":
						producto=Productos.objects.filter(id_proveedor=proveedor).order_by("id")
					else:
						est=Estatus.objects.get(id=pml)
						producto=Productos.objects.filter(id_proveedor=proveedor,publicado_ml=est).order_by("id")
				if estatus>0 and proveedor==0:
					if pml=="":
						producto=Productos.objects.filter(id_estatus=estatus).order_by("id")
					else:
						est=Estatus.objects.get(id=pml)
						producto=Productos.objects.filter(id_estatus=estatus,publicado_ml=est).order_by("id")
				if proveedor>0 and estatus>0:
					if pml=="":
						producto=Productos.objects.filter(id_proveedor=proveedor,id_estatus=estatus).order_by("id")
					else:
						est=Estatus.objects.get(id=pml)
						producto=Productos.objects.filter(id_proveedor=proveedor,id_estatus=estatus,publicado_ml=est).order_by("id")
				if proveedor==0 and estatus==0:
					if pml=="":
						producto=Productos.objects.all().order_by("id")
					else:
						est=Estatus.objects.get(id=pml)
						producto=Productos.objects.filter(publicado_ml=est).order_by("id")
		form=Busqueda_Producto_Form(request.POST)
	else:
		est=Estatus.objects.get(id=1)
		producto=Productos.objects.filter(id_estatus=est).order_by("id")
		form=Busqueda_Producto_Form()
	produ=[]
	for x in producto:
		produ.append({"precio_ml":x.precio_ml,"pml":x.publicado_ml.estatus,"id":x.id,"nombre":x.nombre,"precio":x.precio,"proveedor":x.id_proveedor.proveedor,"marca":x.marca,"id_estatus":x.id_estatus.estatus,"nom_img":str_clave(x.id)})

	return render(request,'inventario/busca_producto.html',locals())

def busca_proveedor(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('seguridad:login'))

	if request.method=="POST":
		proveedor=request.POST.get("nombre_proveedor")
		proveedor=Proveedor.objects.filter(proveedor__icontains=proveedor)
		form=Busca_Proveedores_Form(request.POST)
	else:
		proveedor=Proveedor.objects.all()
		form=Busca_Proveedores_Form()
	return render(request,'inventario/busca_proveedor.html',locals())

def busca_categoria(request):
	categoria=Categorias.objects.all()
	return render(request,'inventario/busca_categoria.html',locals())

#formulario alta de proveedores
def proveedores_edicion_registro(request,id_proveedor=None):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('seguridad:login'))

	if id_proveedor:
		proveedor=Proveedor.objects.get(id=id_proveedor)
	else:
		proveedor=Proveedor()

	if request.method=="POST":
		form=Proveedores_Form(request.POST,instance=proveedor)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventario:busca_proveedor'))
	else:
		form=Proveedores_Form(instance=proveedor)
	return render(request,'inventario/proveedor.html',locals())

def categoria_edicion_registro(request,id_categoria=None):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('seguridad:login'))

	if id_categoria:
		categoria=Categorias.objects.get(id=id_categoria)
	else:
		categoria=Categorias()
	if request.method=="POST":
		form=Categorias_Form(request.POST,instance=categoria)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('inventario:busca_categoria'))
	else:
		form=Categorias_Form(instance=categoria)
	return render(request,'inventario/categoria.html',locals())

#formulario de alta de producto
def registro_edicion_producto(request,id_producto=None):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('seguridad:login'))


	if id_producto:
		producto=Productos.objects.get(id=id_producto)
		folio=str_clave(producto.id)
	else:
		producto=Productos()
		prod=Productos.objects.aggregate(Max("id"))
		try:
			folio=str_clave(int(prod["id__max"])+1)
		except:
			folio=str_clave(1)

	#creamos los formsets
	Atributo_Formset=inlineformset_factory(Productos,Atributos,fields=["atributo","valor_atributo",],extra=1,can_delete=True)
	Talla_Formset=inlineformset_factory(Productos,Tallas,fields=["talla",],extra=1,max_num=10,can_delete=True)

	#imagenes_formset=inlineformset_factory(Productos,Img_Producto,fields=["nom_img","orden",],extra=2,can_delete=False)
	Productos_Relacionados_Formset=inlineformset_factory(Productos,Productos_Relacionados,fields=["id_producto_relacionado",],fk_name="id_producto",extra=1,can_delete=True)
	Rel_Producto_Categoria_Formset=inlineformset_factory(Productos,Rel_Producto_Categoria,fields=["id_producto","id_categoria",],fk_name="id_producto",extra=1,can_delete=True)
	Img_Producto_Formset=inlineformset_factory(Productos,Img_Producto,fields=["nom_img",'orden',],fk_name="id_producto",extra=1,can_delete=True)

	if request.method=="POST":
		consulta=False
		img=""
		form=Productos_Form(request.POST,instance=producto)
		atributo_formset=Atributo_Formset(request.POST,instance=producto)
		talla_formset=Talla_Formset(request.POST,instance=producto)
		productos_relacionados_formset=Productos_Relacionados_Formset(request.POST,instance=producto)
		rel_producto_categoria_formset=Rel_Producto_Categoria_Formset(request.POST,instance=producto)
		img_producto_formset=Img_Producto_Formset(request.POST,instance=producto)
		if form.is_valid() and atributo_formset.is_valid() and talla_formset.is_valid() and productos_relacionados_formset.is_valid() and rel_producto_categoria_formset.is_valid() and img_producto_formset.is_valid():
			form.save()
			atributo_formset.save()
			talla_formset.save()
			productos_relacionados_formset.save()
			rel_producto_categoria_formset.save()
			img_producto_formset.save()
			return HttpResponseRedirect(reverse('inventario:busca_producto'))
	else:
		consulta=True
		try:
			img=Img_Producto.objects.get(id_producto=producto,orden=1).nom_img
		except:
			consulta=False
			img=""
		form=Productos_Form(instance=producto)
		atributo_formset=Atributo_Formset(instance=producto)
		talla_formset=Talla_Formset(instance=producto)
		#imagenes_formset=imagenes_formset(instance=producto)
		productos_relacionados_formset=Productos_Relacionados_Formset(instance=producto)
		rel_producto_categoria_formset=Rel_Producto_Categoria_Formset(instance=producto)
		img_producto_formset=Img_Producto_Formset(instance=producto)
	return render(request,'inventario/producto.html',locals())

def edicion_existencias(request,id_producto=None):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('seguridad:login'))

	if id_producto:
		producto=Productos.objects.get(id=id_producto)
	else:
		producto=Productos()
	Talla_Formset=inlineformset_factory(Productos,Tallas,fields=["talla","entrada","salida","apartado"],extra=0,can_delete=True)
	if request.method=="POST":
		form=Productos_Form(request.POST,instance=producto)
		tallas_formset=Talla_Formset(request.POST,instance=producto)
		if tallas_formset.is_valid():
			tallas_formset.save()
			return HttpResponseRedirect(reverse('inventario:busca_producto'))
	else:
		form=Productos_Form(instance=producto)
		tallas_formset=Talla_Formset(instance=producto)
	return render(request,'inventario/entrada_producto.html',locals())

#esta api se usara sobre todo en la consulta del producto,
#parametro:
#	id: REcibe el id del producto que desea consultar.
#	return: regresa toda la informacion relacionada con el producto que desea consultar.
@api_view(['GET'])
def api_consulta_producto(request):
	producto=[]
	try:
		atributos=[]
		tallas=[]
		img_prod=[]
		p_r=[]
		#parametros

		#print(request.GET.get("id_producto"))

		id_producto=int_clave(request.GET.get("id_producto"))
		#..

		est=Estatus.objects.get(id=1)

		#obtenemos el producto
		prod=Productos.objects.get(id=id_producto,id_estatus=est)

		#obtenemos los atributos del producto
		att=Atributos.objects.filter(id_producto=prod)

		#validamos que contenga atributos
		if att.exists():
			for a in att:
				atributos.append({'atributo':a.atributo,'valor_atributo':a.valor_atributo})

		#obtenemos las tallas del producto
		ta=Tallas.objects.filter(id_producto=prod)

		#validamos que tenga tallas registradas
		if ta.exists():
			for t in ta:

				print(str(t.id_producto.id)+' '+t.talla+' '+str(t.entrada)+' '+str(t.salida))

				#validamos que tenga existencia la talla
				if (t.entrada-t.salida)>0:
					talla=t.talla
					if len(t.talla)==9:
						talla=t.talla+' '
					if len(t.talla)==8:
						talla=t.talla+'  '
					if len(t.talla)==7:
						talla=t.talla+'   '
					if len(t.talla)==6:
						talla=t.talla+'    '
					if len(t.talla)==5:
						talla=t.talla+'     '
					if len(t.talla)==4:
						talla=t.talla+'      '
					if len(t.talla)==3:
						talla=t.talla+'       '
					if len(t.talla)==2:
						talla=t.talla+'        '
					if len(t.talla)==1:
						talla=t.talla+'         '

					tallas.append({'id_talla':t.id,'talla':t.talla+" ("+str(t.entrada-t.salida)+" disp.)"})

		#obtenemos las imagenes del producto
		img=Img_Producto.objects.filter(id_producto=prod).order_by('id')

		#obtenemos los productos relacionados
		prod_r=Productos_Relacionados.objects.filter(id_producto=prod)

		if prod_r.exists():
			for p in prod_r:
				#obtenemos la imagen relacionada que sea orden 1
				#la imagen con orden  1 deberia ser la img principal del producto
				try:
					img_r=Img_Producto.objects.get(id_producto=p.id_producto_relacionado,orden=1)
					p_r.append({'id_producto_relacionado':p.id_producto_relacionado.id,'nombre_producto':p.id_producto_relacionado.nombre,'img_producto_rel':img_r.nom_img,'orden':img_r.orden,'precio':p.id_producto_relacionado.precio})
				except Exception as e:
					print("el producto no tiene productos relacionados con el orden valor=1")
					print(e)
					img_r=[]

		#validamos que tenga imagenes
		if img.exists():
			for i in img:
				img_prod.append({'img_producto':i.nom_img,'orden':i.orden})

		producto.append({'precio':prod.precio,'id_producto':prod.id,'nom_producto':prod.nombre,'desc_producto':prod.desc_producto,'atributos':atributos,'tallas':tallas,'img_prod':img_prod,'descuento':prod.descuento,'prod_relacionado':p_r})
	except Exception as e:
		print(e)
	return Response(producto)

#esta api busca los productos dependiendo de los parametros que se indiquen
#parametros:
#	tipo_busqueda:
#					1=indica que se buscara por la categoria (id_categoria)
#					2= indica que se recibira una palabra y se buscaran los productos que contengan esa palabra en sus atributos
@api_view(['GET'])
def api_busqueda_productos(request):
	productos=[]
	muestra_descuento=0
	if request.method=="GET":
		tipo_busqueda=request.GET.get("tipo_busqueda")
		est=Estatus.objects.get(id=1)#obtenemos el estatus "activo" del catalogo
		if tipo_busqueda=="1":#busqueda por categoria.
			id=request.GET.get("param1")
			try:
				id_categoria=Categorias.objects.get(id=id)
			except Exception as e:
				print (e)#si la categoria no existe, pues no encontramos productos.
				return Response(productos)
			p_e=Rel_Producto_Categoria.objects.filter(id_categoria=id_categoria)
			if p_e.exists():
				for p in p_e:
					try:
						tallas_entrada=Tallas.objects.filter(id_producto=p.id_producto).aggregate(Sum('entrada'))
						tallas_salida=Tallas.objects.filter(id_producto=p.id_producto).aggregate(Sum('salida'))
						cont=int(tallas_entrada["entrada__sum"])-(tallas_salida["salida__sum"])
					except:
						cont=0

					if cont>0:
						if p.id_producto.id_estatus==est:#validamos que el producto este activo
							#imagen=Img_Producto.objects.get(id_producto=p.id_producto,orden=1)
							#precio_desc=decimal.Decimal(p.id_producto.precio)*decimal.Decimal((decimal.Decimal(p.id_producto.descuento)/100.00))
							precio_desc=p.id_producto.precio-(p.id_producto.precio*(decimal.Decimal(p.id_producto.descuento/100.00)))
							if p.id_producto.descuento>0:
								muestra_descuento=1
							else:
								muestra_descuento=0
							productos.append({"descuento":p.id_producto.descuento,"precio_antes":p.id_producto.precio,"id":p.id_producto.id,'str_id':str_clave(p.id_producto.id),"nombre":p.id_producto.nombre,"precio":precio_desc,'muestra_descuento':muestra_descuento})

							
		if tipo_busqueda=="2":#busqueda por palabra
			Productos_Temp.objects.all().delete()

			text_busqueda=request.GET.get("param1").split(" ")	
			cont=0	
			q=None
			q=Productos.objects.filter(desc_producto__icontains=str(request.GET.get("param1")))			
			if q.exists():
				for i in q:
					Productos_Temp.objects.create(id_producto=i.id)
			cad1=""
			cad2=""
			cad3=""
			cad4=""
			cont=0
			#este ciclo ayuda a buscar todas las palabras de busqueda, y hacer la busqueda por separada para cada una de ellas
			for x in text_busqueda:				
				if len(x)>3:					
					if cont<4:
						cont=cont+1				
					if cont==1:
						cad1=x
					if cont==2:
						cad2=x
					if cont==3:
						cad3=x
					if cont==4:
						cad4=x

			if cont==4:	
				cont=cont-1					
				
				q=Productos.objects.filter(desc_producto__icontains=str(cad1)).filter(desc_producto__icontains=str(cad2)).filter(desc_producto__icontains=str(cad3)).filter(desc_producto__icontains=str(cad4))					
				if q.exists():
					for i in q:
						try:
							Productos_Temp.objects.create(id_producto=i.id)				
						except:
							print("el prod ya estaba agregado")
			if cont==3:						
				cont=cont-1
			
				q=Productos.objects.filter(desc_producto__icontains=str(cad1)).filter(desc_producto__icontains=str(cad2)).filter(desc_producto__icontains=str(cad3))
				if q.exists():
					for i in q:
						try:
							Productos_Temp.objects.create(id_producto=i.id)
						except:
							print("el prod ya estaba agregado")
			if cont==2:						
				cont=cont-1
				
				q=Productos.objects.filter(desc_producto__icontains=str(cad1)).filter(desc_producto__icontains=str(cad2))
				if q.exists():
					for i in q:
						try:
							Productos_Temp.objects.create(id_producto=i.id)
						except:
							print("el prod ya estaba agregado")


			if cont==1:
				cont=cont-1
				q=Productos.objects.filter(desc_producto__icontains=str(cad1))

				if q.exists():

					for i in q:
						try:
							Productos_Temp.objects.create(id_producto=i.id)
						except:
							print("el prod ya estaba agregado")

				
			prod=Productos_Temp.objects.all().order_by("id")
		
			#p_e=Rel_Producto_Categoria.objects.filter(id_producto__in=prod)
			if prod==None:
				return Response(productos)
			if prod.exists():
				for p in prod:
					
					try:
						pr=Productos.objects.get(id=p.id_producto)
					except Exception as e:
						print(e)
					#validamos que el producto tenga existencia.
					try:
						tallas_entrada=Tallas.objects.filter(id_producto=pr).aggregate(Sum('entrada'))
						tallas_salida=Tallas.objects.filter(id_producto=pr).aggregate(Sum('salida'))
						cont=int(tallas_entrada["entrada__sum"])-(tallas_salida["salida__sum"])
					except:
						cont=0

					if cont>0:
						if pr.id_estatus==est:#validamos que el producto este activo
							#imagen=Img_Producto.objects.get(id_producto=p.id_producto,orden=1)
							#precio_desc=decimal.Decimal(p.id_producto.precio)*decimal.Decimal((decimal.Decimal(p.id_producto.descuento)/100.00))
							precio_desc=pr.precio-(pr.precio*(decimal.Decimal(pr.descuento/100.00)))
							if pr.descuento>0:
								muestra_descuento=1
							else:
								muestra_descuento=0
							productos.append({"descuento":pr.descuento,"precio_antes":pr.precio,"id":pr.id,'str_id':str_clave(pr.id),"nombre":pr.nombre,"precio":precio_desc,'muestra_descuento':muestra_descuento})
	return Response(productos)

@api_view(['GET'])
def api_busca_prod_x_bloque(request):
	jeans=[]
	blusas=[]
	bolsos=[]
	carteras=[]
	respuesta=[]
	try:
		#obtenemos la categoria jeans
		est_jeans=Categorias.objects.get(id=31)
		p_jeans=Rel_Producto_Categoria.objects.filter(id_categoria=est_jeans)[:2]

		jeans=fn_detalle_producto(p_jeans)

		#obtenemos las categorias blusas
		est_blusas=Categorias.objects.get(id=26)		
		p_blusas=Rel_Producto_Categoria.objects.filter(id_categoria=est_blusas)[:2]

	
		
		blusas=fn_detalle_producto(p_blusas)

		#obtenemos las categorias bolsas
		est_bolsas=Categorias.objects.get(id=39)				
		p_bolsas=Rel_Producto_Categoria.objects.filter(id_categoria=est_bolsas)[:2]

		bolsos=fn_detalle_producto(p_bolsas)

		#obtenemos las categorias carteras
		est_cartera=Categorias.objects.get(id=42)
		p_cartera=Rel_Producto_Categoria.objects.filter(id_categoria=est_cartera)[:2]

		carteras=fn_detalle_producto(p_cartera)

		respuesta.append({"jeans":jeans,"blusas":blusas,"bolsos":bolsos,"carteras":carteras})

	except Exception as e:
		print(e)
	return Response(respuesta)



#api para consultar el catalogo de municipios
@api_view(['GET'])
def api_get_municipios(request):
	cat_municipio=[]
	try:
		mun=Municipio.objects.all()
		for m in mun:
			cat_municipio.append({'id_municipio':m.id,'municipio':m.municipio})
	except Exception as e:
		print(e)
	return Response(cat_municipio)

def str_clave(id):
	if len(str(id))==1:
		return '000000'+str(id)
	if len(str(id))==2:
		return '00000'+str(id)
	if len(str(id))==3:
		return '0000'+str(id)
	if len(str(id))==4:
		return '000'+str(id)
	if len(str(id))==5:
		return '00'+str(id)
	if len(str(id))==6:
		return '0'+str(id)
	if len(str(id))==7:
		return str(id)

def int_clave(id):
	return int(id)

def fn_detalle_producto(obj):
	productos=[]
	est=Estatus.objects.get(id=1)#obtenemos el estatus "activo" del catalogo
	if obj.exists():
				for p in obj:
					try:
						tallas_entrada=Tallas.objects.filter(id_producto=p.id_producto).aggregate(Sum('entrada'))
						tallas_salida=Tallas.objects.filter(id_producto=p.id_producto).aggregate(Sum('salida'))
						cont=int(tallas_entrada["entrada__sum"])-(tallas_salida["salida__sum"])
					except:
						cont=0

					if cont>0:
						if p.id_producto.id_estatus==est:#validamos que el producto este activo
							#imagen=Img_Producto.objects.get(id_producto=p.id_producto,orden=1)
							#precio_desc=decimal.Decimal(p.id_producto.precio)*decimal.Decimal((decimal.Decimal(p.id_producto.descuento)/100.00))
							precio_desc=p.id_producto.precio-(p.id_producto.precio*(decimal.Decimal(p.id_producto.descuento/100.00)))
							if p.id_producto.descuento>0:
								muestra_descuento=1
							else:
								muestra_descuento=0
							productos.append({"descuento":p.id_producto.descuento,"precio_antes":p.id_producto.precio,"id":p.id_producto.id,'str_id':str_clave(p.id_producto.id),"nombre":p.id_producto.nombre,"precio":precio_desc,'muestra_descuento':muestra_descuento})
	return productos

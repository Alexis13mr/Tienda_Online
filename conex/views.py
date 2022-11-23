from django.shortcuts import render,HttpResponse, redirect
from .models import item,compra
# Create your views here.

def inicio(request):
    prod=item.objects.all()    
    return render(request, "Inicio.html",{'prod':prod})
    
def prod(request,pk):
    prod=item.objects.get(id=pk)
    return render(request, 'product.html',{'prod':prod})

def comprar(request,pk):
    prod=item.objects.get(id=pk)
    if request.method=="POST":
        num=1
        nombre=request.POST["nombre"]
        correo=request.POST["correo"]
        direc=request.POST["direccion"]
        id_p=item.objects.get(id=pk)
        desc="N/A"
        cant=1
        vlr=prod.valor
        dat=compra(num_comp= num, nom_cli=nombre,email=correo,direccion=direc,id_prod=id_p,descrip=desc,cantidad=cant,valorcomp=vlr)
        dat.save()
        prod.cant-=1
        prod.save()
        return redirect('Init')
    else:
        prod=item.objects.get(id=pk)

        return render(request, 'compr.html',{'prod':prod})

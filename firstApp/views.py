from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import Product

from .prod_form import ProductForm

# Create your views here.
def one(request):
    print(request.method)
    return HttpResponse('Dei botu this is /myapp/one da ')

def two(request):
    itemCount=[i for i in range(20)]
    return render(request,'home2.html',{'count':itemCount})

def product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        cat=request.POST.get('cat')
        sdesc=request.POST.get('sdesc')
        ldesc=request.POST.get('ldesc')

        Product.objects.create(name=name,price=price,category=cat,s_desc=sdesc,l_desc=ldesc)

        return redirect('one')
    
    return render(request,'product.html')


def product2(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('two')
    else:
        form=ProductForm()
    return render(request,'product.html',{'form':form})
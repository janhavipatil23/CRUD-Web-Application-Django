from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
import csv

# Create your views here.
def show(request):  
    products = Product.objects.all()  
    return render(request,"show.html",{'products':products})  

def prod(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass
    else:  
        form = ProductForm()  
    return render(request,'index.html',{'form':form})  
  

def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product})  

def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product})  

def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/show")  

def export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['Product ID', 'Product Name', 'Product Description', 'Product Quantity', 'Product Price'])
    for product in Product.objects.all().values_list('pid','pname','pdescription','pqty','price'):
        writer.writerow(product)
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    return response







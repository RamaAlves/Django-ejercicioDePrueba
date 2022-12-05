from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound

from .models import Product
from .forms import ProductForm

# Create your views here.
def index(request):

    products = Product.objects.all()

    paginator = Paginator(products,2)
    
    page_number = request.GET.get('page')

    try:
        products_page = paginator.page(page_number) #get_page ya realiza internamente esta validacion
    except PageNotAnInteger:
        print ("Error page not an integer")
        products_page = paginator.page(1)
    except EmptyPage:
        print ("Error page not found")
        products_page = paginator.page(1)

    return render(request, 'index.html', {'products': products_page})

def show(request, pk):

    """ try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        print ("Error product does not exist")
        #return HttpResponse(status=404)
        return HttpResponseNotFound """
    
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'show.html', {'product': product})

def create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print("valido")

            product = Product()

            product.title=form.cleaned_data['title']
            product.description=form.cleaned_data['description']
            product.price=form.cleaned_data['price']
            product.category=form.cleaned_data['category']

            product.save()
            print("product save:", product)
            return redirect('gestion:update', pk=product.id)

        else:
            print("invalido")

    return render(request, 'save.html', {'form': form})

def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    form = ProductForm(initial={'title':product.title,'description':product.description,'price':product.price,'category':product.category})
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        
        if form.is_valid():
            print("valido")

            product.title=form.cleaned_data['title']
            product.description=form.cleaned_data['description']
            product.price=form.cleaned_data['price']
            product.category=form.cleaned_data['category']

            product.save()
            print("product update:", product)

            return redirect('gestion:index')

        else:
            print("invalido")

    return render(request, 'save.html', {'form': form})

def delete(request, pk):

    product = get_object_or_404(Product, pk=pk)
    print("Product delete: ", product)
    product.delete()
    return redirect('gestion:index')
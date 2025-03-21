from django.shortcuts import HttpResponse,render
from store.models import Product 

def home(request):
    # return HttpResponse("This is home page .....")
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
    }
    return render(request,'home.html',context)
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Laptop,Category
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('./register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('./register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('./login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('./register')
        return redirect('/')
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')       


def home(request):
    lists =Laptop.objects.all()
    return render(request,'home.html',{'lists':lists})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html',)

def product_create_view(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        p=form.save(commit=False)
        p.save()
        a = Category(name = p)
        a.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Laptop, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)


def category_list_view(request):
    
    queryset = Category.objects.all() 
    context = {
        "object_list": queryset
    }
    print(queryset)
    return render(request, "category_list.html", context)
def product_list_view(request):
    queryset = Laptop.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "product_list.html", context)

def category_detail_view(request, id):
    obj = get_object_or_404(Category, id=id)
    context = {
        "object": obj
    }
    return render(request, "category_details.html", context)


def product_detail_view(request, id):
    obj = get_object_or_404(Laptop, id=id)
    context = {
        "object": obj
    }
    return render(request, "product_details.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Laptop, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "product_delete.html", context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.
def index_shop(request):
    products = Product.objects.all()
    return render(request, "shop/index.html", {"products": products})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("با موفقیت وارد شدید"))
            return redirect("index_shop")
        else:
            messages.error(request, ("ورود با خطا مواجه شده است"))
            return redirect("login_url")

    else:
        return render(request, "shop/login.html")


def signup_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            user = authenticate(request, username=username, passoword=password1)
            if user is not None:
                login(request, user)
                messages.success(request, (" اکانت با موفقیت ساخته شد"))
                return redirect("index_shop")
            else:
                messages.warning(
                    request, ("اکانت ساخته شد اما دوباره برای وارد شدن تلاش کنید")
                )
                return redirect("index_shop")
        else:
            messages.error(request, ("دوباره سعی کنید"))
            return redirect("signup_url")
    else:
        return render(request, "shop/signup.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, ("با موفقیت خارج شدید"))
    return redirect("index_shop")


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "shop/product.html", {"product": product})


def category(request, cat=None):
    if cat is not None:
        cat = cat.replace("-", " ")
    try:

        category = Category.objects.get(name=cat)  # programing
        products = Product.objects.filter(category=category)
        return render(request, "shop/category.html", {"products": products})
    except:
        messages.error(request, ("دسته بندی وجود ندارد"))
        return render(request, "shop/includes/404.html")


def search_course(request):
    pass

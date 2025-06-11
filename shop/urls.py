from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_shop, name="index_shop"),
    path("error_category", views.category, name="errorPage"),
    path("login/", views.login_user, name="login_url"),
    path("signup/", views.signup_user, name="signup_url"),
    path("logout/", views.logout_user, name="logout_url"),
    path("product/<int:pk>", views.product, name="product"),
    path("category/<str:cat>", views.category, name="category_url"),
    
]

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product-category/<str:slug>', views.product_category, name='product-category'),
    path('more_info/<int:id>/', views.more_info, name='more_info'),
]

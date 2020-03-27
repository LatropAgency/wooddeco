from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('', views.my_account, name='my-account'),
    path('authorization/', views.authorization, name='authorization'),
    path('registration/', views.registration, name='registration'),
    path('edit-account/', views.EditAccount.as_view(), name='edit-account'),
    path('logout/', views.logout, name='logout'),
]

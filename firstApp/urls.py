from django.urls import path
from . import views

urlpatterns=[
    path('one/',views.one,name='one'),
    path('two/',views.two,name='two'),
    path('product',views.product,name='product'),
    path('product2',views.product2,name='product2')

]
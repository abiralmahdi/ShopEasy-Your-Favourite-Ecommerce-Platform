from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('category/<str:category>/', views.products_page, name='products_page'),
    path('category/<str:category>/<str:product>', views.indiv_product, name='indiv_product'),
    path('add_to_cart/<str:product>/<str:qty>', views.add_to_cart, name='add_to_cart'),
    path('checkout/<str:amount>/', views.trigger_checkout, name='trigger_checkout'),
    path('fail/', views.failed_transanction, name='fail'),
    path('success/<str:user_id>', views.successful_transanction, name='success'),
]
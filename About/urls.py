from django.urls import path

from . import views
urlpatterns=[
    path('About',views.About,name='About'),
    path('Contact_Us',views.Contact_Us,name='Contact_Us')
]
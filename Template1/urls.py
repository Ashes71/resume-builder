from django.urls import path

from . import views
urlpatterns=[
    path('Template1',views.Template1,name='template'),
    path('Template1/Template1_About', views.Template1_About, name='About'),
    path('Template1/Template1_Contact_Us', views.Template1_Contact_Us, name='Contact_Us')
]

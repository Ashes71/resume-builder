from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('Template1',views.Template1,name='template'),
    path('Template1/Template1_About', views.Template1_About, name='About'),
    path('Template1/Template1_Contact_Us', views.Template1_Contact_Us, name='Contact_Us')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

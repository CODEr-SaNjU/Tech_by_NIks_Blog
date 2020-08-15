from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('Blogs/',views.Blogs,name="Blogs"),
    path('About/',views.About,name="About"),
    path('Contact/',views.Contact,name="Contact"),
    path('blogdetails/<int:id>/',views.DetalView,name="DetalView"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
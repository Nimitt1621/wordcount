
from django.contrib import admin
from django.urls import path
from first_app import views
urlpatterns = [
    path('',views.index,name='home'),
    path('admin/', admin.site.urls),
    path('count/', views.count, name='dead'),
    path('about/', views.about, name='about'),
]

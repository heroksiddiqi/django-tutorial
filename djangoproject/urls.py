from django.contrib import admin
from django.urls import path
from djangomvctutorial import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.hello, name="hello"),
]

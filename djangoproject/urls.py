from django.contrib import admin
from django.urls import path
#3 import view file from appname['djangomvctutorial']
from djangomvctutorial import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.hello, name="hello"), #path() is the route url. parameters: path('url', view_function, optional name)
    #4 now if you go to "http://127.0.0.1:8000/index/" , you will be greeted with hello world
]


from django.contrib import admin
from django.urls import path, include
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Home Page")

# def room(request):
#     return HttpResponse("Room")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name="home"),
    # path('room/', room, name="room")
    path("", include('base.urls'))
]
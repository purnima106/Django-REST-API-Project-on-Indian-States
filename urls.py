from django.contrib import admin
from django.urls import path, include
from capapp.views import home
from rest_framework.routers import DefaultRouter
from capapp.views import IndianStateViewSet

router = DefaultRouter()
router.register(r'indian-states', IndianStateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path('api/', include(router.urls)),
   
]

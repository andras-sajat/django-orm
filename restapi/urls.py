from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include, url
from .api.resources import PersonResource
from restapi.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

person_resource = PersonResource()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(person_resource.urls)),
]
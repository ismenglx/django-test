from django.urls import path, include
from rest_framework_mongoengine import routers

from mongoengineTest.util.select import test
from mongoengineTest.views import AuthorViewSet, index

router = routers.DefaultRouter()
router.register(r'all', AuthorViewSet, base_name='author')
# router.register(r'retrieve', AuthorViewSet)

urlpatterns = [
    path('index/', index),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

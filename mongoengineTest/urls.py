from django.urls import path, include
from rest_framework_mongoengine import routers

from mongoengineTest.views import AuthorViewSet, index

router = routers.DefaultRouter()
router.register('all', AuthorViewSet, base_name='author')

urlpatterns = [
    # path('<str:name>/', SelectView.get),
    path('index/', index),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter

cate_router = DefaultRouter()
cate_router.register(r'core', CategoryViewSet, basename='core')
urlpatterns = cate_router.urls


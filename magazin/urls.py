from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from core.views import product_list, sotrudnik_list, product_list_api, CategoryCreateView, SotrudnikiCreateView, CategoryView, ProductView
from core.views import ProductView, CategoryView
from custom_auth.views import RegisterView, LoginView
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    # path('', product_list),
    # path('sotrudnik/', sotrudnik_list),
    # path('product_list/', product_list_api),
    # path('category/create/', CategoryCreateView.as_view()),
    # path('sotrudniki/create/', SotrudnikiCreateView.as_view()),
    path('', ProductView.as_view({'get' : 'list', 'post' : 'create'})),
    path('<int:pk>', ProductView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    path('category/', CategoryView.as_view({'get' : 'list', 'post' : 'create'})),
    path('category/<int:pk>', CategoryView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

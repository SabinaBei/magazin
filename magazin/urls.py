from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import product_list, sotrudnik_list, product_list_api, CategoryCreateView, SotrudnikiCreateView, CategoryView, ProductView
from core.views import ProductView, CategoryView
from custom_auth.views import RegisterView, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list),
    path('sotrudnik/', sotrudnik_list),
    path('product_list/', product_list_api),
    path('category/create/', CategoryCreateView.as_view()),
    path('sotrudniki/create/', SotrudnikiCreateView.as_view()),
    path('product/', ProductView.as_view({'get' : 'list', 'post' : 'create'})),
    path('product/<int:pk>', ProductView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    path('category/', CategoryView.as_view({'get' : 'list', 'post' : 'create'})),
    path('category/<int:pk>', CategoryView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

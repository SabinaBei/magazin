#логика отображения web-страницы

from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Products, Sotrudniki, Category
from core.serializers import ProductSerializer, CategorySerializer
from core.forms import CategoryForms, SotrudnikiForms
from core.permissions import ProductPermission


def product_list(request):
    product = Products.objects.all()
    return render(
        request,
        'main.html',
        {
            'products': product
        }
    )

def sotrudnik_list(request):
    sotrudnik = Sotrudniki.objects.all()
    return render(
        request,
        'sotrudnik.html',
        {
            'sotrudniki': sotrudnik
        }
    )

@csrf_exempt
def product_list_api(request):
    """
        List all courses or create a new course
    """
    if request.method == 'GET':
        product = Products.objects.all()
        serializer = ProductSerializer(instance=product, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


class ProductListMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Products
        fields = ['category']


class ProductView(ModelViewSet):
    queryset = Products.objects.all().order_by('-id')   #srez ob'ektov, kotorii nujno vivodit
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description', 'price']
    ordering_fields = ['price', 'name', 'description']
    filterset_class = ProductFilter
    permission_classes = (ProductPermission)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForms
    template_name = 'category.html'
    success_url = '/category/create/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category'] = category
        return context


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()   #srez ob'ektov, kotorii nujno vivodit
    serializer_class = CategorySerializer
    # lookup_field = 'pk'

# class CategoryDetailView(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailCreateUpdateSerializer

# class CategoryUpdateView(UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailCreateUpdateSerializer
#
# class CategoryDeleteView(DestroyAPIView):
#     queryset = Category.objects.all()

class SotrudnikiCreateView(generic.CreateView):
    model = Sotrudniki
    form_class = SotrudnikiForms
    template_name = 'sotrudniki.html'
    success_url = '/sotrudniki/create/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Sotrudniki.objects.all()
        context['sotrudniki'] = category
        return context

# ispolzuetsya dlya napisaniya vsei logiki


from rest_framework import viewsets
# from core.serializer import CategorySerializers
# from .models import About


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

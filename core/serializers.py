from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from core.models import Products, Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'image', 'category', 'user')
        extra_kwargs = {'user': {'read_only': True}}
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Products.objects.all(),
        #         fields=['name', 'price']
        #     )
        # ]

    # def to_representation(self, instance):
    #     # print(instance)
    #     response = super().to_representation(instance)
    #     # print(response)
    #     serializers_category = CategorySerializer(instance=instance.category)
    #     print(serializers_category)
    #     response["category"] = serializers_category.data
    #     return response
from django.forms import ModelForm
from core.models import Category, Sotrudniki

class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SotrudnikiForms(ModelForm):
    class Meta:
        model = Sotrudniki
        fields = ['name', 'surname', 'email', 'telephone']

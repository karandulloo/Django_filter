import django_filters
from django_filters import CharFilter , NumberFilter
from .models import *

class EmblFilter(django_filters.FilterSet):
    coexpression = NumberFilter(field_name='coexpression')
    protein1 = CharFilter(field_name='protein1' , lookup_expr='icontains'  , label='Protein1')
    protein2 = CharFilter(field_name='protein2' , lookup_expr='icontains' , label='Protein2')
    neighborhood = NumberFilter(field_name='neighborhood')
    fusion = NumberFilter(field_name='fusion')
    cooccurence = NumberFilter(field_name='cooccurence')
    experimental = NumberFilter(field_name='experimental')
    database = NumberFilter(field_name='database')
    textmining = NumberFilter(field_name='textmining')
    combined_score = NumberFilter(field_name='combined_score')
    class Meta:
        model = Embl
        fields = '__all__'
        # exclude = ['protein1' , 'protein2']
    
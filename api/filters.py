import django_filters
from .models import Kiralama

class KiralamaFilter(django_filters.FilterSet):
    iha_id = django_filters.NumberFilter(field_name='iha__id')
    kiralayan_uye = django_filters.CharFilter(field_name='kiralayan_uye__username')
    baslangic_tarihi_gte = django_filters.DateFilter(field_name='baslangic_tarihi', lookup_expr='gte')
    baslangic_tarihi_lte = django_filters.DateFilter(field_name='baslangic_tarihi', lookup_expr='lte')
    class Meta:
        model = Kiralama
        fields = ['iha_id', 'kiralayan_uye', 'baslangic_tarihi_gte', 'baslangic_tarihi_lte']
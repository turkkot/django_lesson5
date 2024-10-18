import django_filters
import studentWorksPlatform.models
from django.db.models import Q

class Work(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Цена от и до')
    term = django_filters.CharFilter(method='filter_term', label='')

    class Meta:
        model = studentWorksPlatform.models.Work
        fields = ['price_range', 'term']

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(title__icontains=term) | Q(description__icontains=term)

        return queryset.filter(criteria).distinct()



class UserFilter(django_filters.FilterSet):
    is_banned = django_filters.BooleanFilter(field_name='is_banned', label='Пользователь забанен?')
    term = django_filters.CharFilter(method='filter_term', label='Поиск по имени или email')

    class Meta:
        model = studentWorksPlatform.models.User
        fields = ['is_banned', 'term']

    def filter_is_banned(self, queryset, name, value):
        return queryset.filter(is_banned=value)

    def filter_term(self, queryset, name, value):
        if not value:
            return queryset

        criteria = Q()
        for term in value.split():
            criteria |= Q(username__icontains=term) | Q(email__icontains=term)

        return queryset.filter(criteria).distinct()

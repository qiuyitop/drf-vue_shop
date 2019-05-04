import django_filters

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    '''
    商品过滤的类
    '''
    # 两个参数，name是要过滤的字段，lookup是执行的行为，‘小与等于本店价格’
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    search_field = django_filters.CharFilter(field_name='name', lookup_expr='contains')
    ordering = django_filters.OrderingFilter(fields=('sold_num', 'add_time'),
                                             field_labels={'sold_num': '销量', 'add_time': '添加时间'})

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
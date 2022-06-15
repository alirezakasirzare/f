from django.urls import path
from . import api_views

app_name = 'ApiSellerPanel'

urlpatterns = [
    path('sellerpanel-shop-add/', api_views.sellerpanel_shop_add.as_view(), name='sellerpanel_shop_add'),
    path('sellerpanel-edit-account/', api_views.sellerpanel_edit_account.as_view(), name='sellerpanel_edit_account'),
    path('sellerpanel-user-info/', api_views.sellerpanel_user_info.as_view(), name='sellerpanel_user_info'),
    path('sellerpanel-products-add/', api_views.sellerpanel_products_add.as_view(), name='sellerpanel_products_add'),
    path('sellerpanel-products-edit/', api_views.sellerpanel_products_edit.as_view(), name='sellerpanel_products_edit'),
    path('sellerpanel-products-delete/', api_views.sellerpanel_products_delete.as_view(), name='sellerpanel_products_delete'),
    path('sellerpanel-products-list/', api_views.sellerpanel_products_list.as_view(), name='sellerpanel_products_list'),
    path('sellerpanel-products-comments-list/', api_views.sellerpanel_products_comments_list.as_view(), name='sellerpanel_products_comments_list'),
    path('sellerpanel-products-orders-list/', api_views.sellerpanel_products_orders_list.as_view(), name='sellerpanel_products_orders_list'),
    path('sellerpanel-products-complaints-list/', api_views.sellerpanel_products_complaints_list.as_view(), name='sellerpanel_products_complaints_list'),
    path('sellerpanel-products-complaints-user-info/', api_views.sellerpanel_products_complaints_user_info.as_view(), name='sellerpanel_products_complaints_user_info'),
    path('sellerpanel-products-sales-chart-day/', api_views.sellerpanel_products_sales_chart_day.as_view(), name='sellerpanel_products_sales_chart_day'),
    path('sellerpanel-products-sales-chart-week/', api_views.sellerpanel_products_sales_chart_week.as_view(), name='sellerpanel_products_sales_chart_week'),
    path('sellerpanel-products-sales-chart-month/', api_views.sellerpanel_products_sales_chart_month.as_view(), name='sellerpanel_products_sales_chart_month'),
    path('sellerpanel-products-sales-chart-year/', api_views.sellerpanel_products_sales_chart_year.as_view(), name='sellerpanel_products_sales_chart_year'),
    path('sellerpanel-messages-add/', api_views.sellerpanel_messages_add.as_view(), name='sellerpanel_messages_add'),
    path('sellerpanel-messages-list-filter/', api_views.sellerpanel_messages_list_filter.as_view(), name='sellerpanel_messages_list_filter'),
    path('sellerpanel-users-messages-list/', api_views.sellerpanel_users_messages_list.as_view(), name='sellerpanel_users_messages_list'),
]
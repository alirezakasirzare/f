from django.urls import path
from . import api_views

app_name = 'ApiServicePanel'

urlpatterns = [
    path('servicepanel-edit-account/', api_views.servicepanel_edit_account.as_view(), name='servicepanel_edit_account'),
    path('servicepanel-user-info/', api_views.servicepanel_user_info.as_view(), name='servicepanel_user_info'),
    path('servicepanel-service-add/', api_views.servicepanel_service_add.as_view(), name='servicepanel_service_add'),
    path('servicepanel-service-edit/', api_views.servicepanel_service_edit.as_view(), name='servicepanel_service_edit'),
    path('servicepanel-service-delete/', api_views.servicepanel_service_delete.as_view(), name='servicepanel_service_delete'),
    path('servicepanel-service-list/', api_views.servicepanel_service_list.as_view(), name='servicepanel_service_list'),
    path('servicepanel-service-complaints-list/', api_views.servicepanel_service_complaints_list.as_view(),name='sellerpanel_products_complaints_list'),
    path('servicepanel-service-complaints-user-info/', api_views.servicepanel_service_complaints_user_info.as_view(),name='sellerpanel_products_complaints_user_info'),
    path('servicepanel-service-comments-list/', api_views.servicepanel_service_comments_list.as_view(),name='servicepanel_service_comments_list'),
    path('servicepanel-service-orders-list/', api_views.servicepanel_service_orders_list.as_view(),name='servicepanel_service_performed_list'),
    path('servicepanel-service-sales-chart-day/', api_views.servicepanel_service_sales_chart_day.as_view(),name='servicepanel_service_sales_chart_day'),
    path('servicepanel-service-sales-chart-week/', api_views.servicepanel_service_sales_chart_week.as_view(),name='servicepanel_service_sales_chart_week'),
    path('servicepanel-service-sales-chart-month/', api_views.servicepanel_service_sales_chart_month.as_view(),name='servicepanel_service_sales_chart_month'),
    path('servicepanel-service-sales-chart-year/', api_views.servicepanel_service_sales_chart_year.as_view(),name='servicepanel_service_sales_chart_year'),
    path('servicepanel-messages-add/', api_views.servicepanel_messages_add.as_view(), name='servicepanel_messages_add'),
    path('servicepanel-messages-list-filter/', api_views.servicepanel_messages_list_filter.as_view(),name='servicepanel_messages_list_filter'),
    path('servicepanel-users-messages-list/', api_views.servicepanel_users_messages_list.as_view(),name='servicepanel_users_messages_list'),
    path('servicepanel-create-link-payment/', api_views.servicepanel_create_link_payment.as_view(),name='servicepanel_create_link_payment'),
]

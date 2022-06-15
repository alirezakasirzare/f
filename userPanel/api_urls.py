from django.urls import path
from . import api_views

app_name = 'ApiUserPanel'

urlpatterns = [
    path('userpanel-edit-account/',api_views.userpanel_edit_account.as_view(),name='userpanel_edit_account'),
    path('userpanel-user-info/',api_views.userpanel_user_info.as_view(),name='userpanel_user_info'),
    path('userpanel-order-history/',api_views.userpanel_order_history.as_view(),name='userpanel_order_history'),
    path('userpanel-services-received/',api_views.userpanel_services_received.as_view(),name='userpanel_services_received'),
    path('userpanel-products-scores-list/',api_views.userpanel_products_scores_list.as_view(),name='userpanel_products_scores_list'),
    path('userpanel-products-comments-list/',api_views.userpanel_products_comments_list.as_view(),name='userpanel_products_comments_list'),
    path('userpanel-seller-messages-add/',api_views.userpanel_seller_messages_add.as_view(),name='userpanel_seller_messages_add'),
    path('userpanel-seller-messages-list-filter/',api_views.userpanel_seller_messages_list_filter.as_view(),name='userpanel_seller_messages_list_filter'),
    path('userpanel-seller-users-messages-list/',api_views.userpanel_seller_users_messages_list.as_view(),name='userpanel_seller_users_messages_list'),
    path('userpanel-service-messages-add/', api_views.userpanel_service_messages_add.as_view(),name='userpanel_service_messages_add'),
    path('userpanel-service-messages-list-filter/', api_views.userpanel_service_messages_list_filter.as_view(),name='userpanel_service_messages_list_filter'),
    path('userpanel-service-users-messages-list/', api_views.userpanel_service_users_messages_list.as_view(),name='userpanel_service_users_messages_list'),
]
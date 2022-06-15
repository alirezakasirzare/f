from django.urls import path
from . import api_views

app_name = 'ApiServices'

urlpatterns = [
    path('services-list/', api_views.services_list.as_view(), name='services_list'),
    path('services-detail/', api_views.services_detail.as_view(), name='services_detail'),
    path('services-search/', api_views.services_search.as_view(), name='services_search'),
    path('services-filter/', api_views.services_filter.as_view(), name='services_filter'),
    path('services-best/', api_views.services_best.as_view(), name='services_best'),
    path('services-sliders/', api_views.services_sliders.as_view(), name='services_sliders'),
    path('services-similar/', api_views.services_similar.as_view(), name='services_similar'),
    path('services-comments-list/', api_views.services_comments_list.as_view(), name='services_comments_list'),
    path('services-comments-add/', api_views.services_comments_add.as_view(), name='services_comments_add'),
    path('services-scores-number/', api_views.services_scores_number.as_view(), name='services_scores_number'),
    path('services-scores-search/', api_views.services_scores_search.as_view(), name='services_scores_search'),
    path('services-scores-add/', api_views.services_scores_add.as_view(), name='services_scores_add'),
    path('services-complaints-add/', api_views.services_complaints_add.as_view(),name='services_complaints_add'),
    path('services-categories-list/', api_views.services_categories_list.as_view(),name='services_categories_list'),
    path('services-filter-category/', api_views.services_filter_category.as_view(),name='services_filter_category'),
]
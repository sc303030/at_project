from django.urls import path
from at_project.views import *

app_name = 'at_project'
urlpatterns = [
    # 경현
    path('k-food-report', IndexViews.as_view(), name='k-food-report'),
    path('idol/', AboutViews.as_view(), name='idol'),
    path('food-recipe-2/', AboutViews.as_view(), name='food-recipe-2'),
    path('k-tour/', AboutViews.as_view(), name='k-tour'),

    # 지원
    path('', '', name='index'),
    path('k-food-report-graph', '', name='k-food-report-graph'),
    path('food-recipe/', '', name='food-recipe'),
]
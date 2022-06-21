from django.urls import path, include
from home import views

urlpatterns = [
    path('test/', views.home_index, name="home_index"),
    path('demo-test/', views.home_demo_index, name="home_demo_index"),
    path('simple/', views.home_simple_index, name="home_simple_index"),

    path('query/', views.home_query, name="home_query"),
    path('doquery/', views.home_doquery, name="home_doquery"),
    path('ajax/',views.home_ajax, name="home_ajax"),


    # path('echarts_data/',views.echarts_data, name="echarts_data"),
]
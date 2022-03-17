from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('', views.BaseIndexView.as_view(), name='index'),
    path('chart/', views.FusionChartView.as_view(), name='chart'),
    path('real-time/', views.RealTimeChartView.as_view(), name='real_time'),
]

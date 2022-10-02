from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('', views.BaseIndexView.as_view(), name='index'),
    path('export_to_csv/', views.export_sensor_data_csv, name='export_sensor_data_csv'),
    # path('start_sensor_reading/', views.start_sensor_reading, name='start_sensor_reading'),
]

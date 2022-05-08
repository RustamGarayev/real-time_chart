from django.urls import re_path
from graph_socket import consumers

websocket_urlpatterns = [
    re_path(r'^ws/graph/$', consumers.GraphConsumer.as_asgi(), name="graph-consumer"),
]

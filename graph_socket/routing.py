from django.conf.urls import url
from graph_socket import consumers

websocket_urlpatterns = [
    url(r'^ws/graph/$', consumers.GraphConsumer.as_asgi(), name="graph-consumer"),
]

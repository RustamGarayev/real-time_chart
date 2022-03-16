from graph_socket import consumers

app_name = 'chat_socket'

websocket_urlpatterns = [
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi(), name="chat-room-consumer"),
]
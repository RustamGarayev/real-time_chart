from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# API urls
urlpatterns += [
    path('api/v1/', include('api.urls')),
    path('api-schema/', get_schema_view(
        title="Real-time Chart",
        description="API developed to show real-time chart",
    ), name='api-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'api-schema'}
    ), name='swagger-ui'),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

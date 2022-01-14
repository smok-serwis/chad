from django.conf.urls.static import static
from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings

urlpatterns = [
   path(r'schema/', SpectacularAPIView.as_view(), name='schema'),
   path(r'swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

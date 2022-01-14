from django.conf.urls.static import static
from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
   path('v1/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
   path('v1/', include('documentation.urls')),
   path(r'schema/', SpectacularAPIView.as_view(), name='schema'),
   path(r'swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

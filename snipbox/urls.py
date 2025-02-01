from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from snippets.views import RegenerateTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/regenerate/', RegenerateTokenView.as_view(), name='token_regenerate'),

]

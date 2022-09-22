from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/profiles/', include('profiles.urls')),
    path('api/v1/payments/', include('payments.urls')),
    path('api/v1/photos/', include('photos.urls')), 
    path('api/v1/stats/', include('stats.urls')), 
    # auth
    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/verify/', TokenVerifyView.as_view()),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),    
]

handler404 = 'utils.error_views.handler404'
handler500 = 'utils.error_views.handler500'
handler403 = 'utils.error_views.handler403'

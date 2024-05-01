from django.contrib import admin
from django.urls import path, include, re_path

from doctors.views import logout_user

urlpatterns = [
    # OAuth
    re_path('auth/', include('drf_social_oauth2.urls', namespace='drf')),

    # DRF
    path('api-auth/', include('rest_framework.urls')),

    # Django Password Reset
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path("admin/", admin.site.urls),
    path("doctor/", include('doctors.urls')),
    path('patient/', include('patients.urls')),
    path('logout/', logout_user, name='logout'),
]

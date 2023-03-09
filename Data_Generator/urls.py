from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from dashboard.views import DashboardView
from users_login.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('<user_name>/', DashboardView.as_view(), name='home'),
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

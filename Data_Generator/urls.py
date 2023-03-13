from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from dashboard.views import DashboardView, CreateSchemaView, EditSchemaView, logout_view, deleteSchema
from users_login.views import CustomLoginView
from generator.views import DataGenerator, downloadCSV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('<user_name>/', DashboardView.as_view(), name='home'),
    path('<user_name>/create', CreateSchemaView.as_view(), name='create'),
    path('<user_name>/edit-schema/<id>', EditSchemaView.as_view(), name='edit'),
    path('<user_name>/generator/<id>', DataGenerator.as_view(), name='generator'),
    path('<user_name>/download/<file_id>', downloadCSV, name='download'),
    path('<user_name>/delete/<id>', deleteSchema, name='delete'),
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

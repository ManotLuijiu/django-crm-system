from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico"))),
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('leads/', include('leads.urls', namespace="leads"))
]

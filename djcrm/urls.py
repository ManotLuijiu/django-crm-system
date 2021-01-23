from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico"))),
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('leads/', include('leads.urls', namespace="leads"))
]

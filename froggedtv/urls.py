from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("www.urls")),
    path(
        "login/",
        views.LoginView.as_view(template_name="pages/login.html"),
        name="login",
    ),
    path("martor/", include("martor.urls")),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

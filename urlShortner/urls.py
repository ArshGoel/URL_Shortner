from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from Services.views import redirect_to_target_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",TemplateView.as_view(template_name = "home.html")),
    path("auth/", include('Accounts.urls')),
    path("dashboard/", include('Services.urls')),
    path("<str:alias>", redirect_to_target_page)
]

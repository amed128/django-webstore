"""webstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from eboutique import views as main_views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index),
    path('eboutique/', include('eboutique.urls')),
    path('client/', include('client.urls')),
    path('account/', include('account.urls')),

    path("password-reset/", auth_views.PasswordResetView.as_view( template_name="account/password_reset.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view( template_name="account/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view( template_name="account/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view( template_name="account/password_reset_complete.html"), name="password_reset_complete"),
    # path('accounts/', include('django.cntrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

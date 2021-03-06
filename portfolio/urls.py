"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from judith import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('otracosa/', admin.site.urls),
    path('portfolio/', views.PortfolioViewEn.as_view(), name='portfolio-en'),
    path('portafolio/', views.PortfolioViewEs.as_view(), name='portfolio-es'),
    path('thanks/', views.ThanksView.as_view(), name='credits'),
    path('', views.HomepageView.as_view(), name='index')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

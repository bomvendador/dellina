"""dfacade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
# from django.urls import path
from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.index_view, name="index"),
    url(r'portfolio_details/(?P<project_id>\d+)/$', views.portfolio_details_view, name="portfolio_details"),
    url(r'contacts/', views.contacts, name="contacts"),
    url(r'compet/', views.goto_compet, name="goto_compet"),
    url(r'projects/', views.goto_project, name="goto_projects"),
    url(r'why_us/', views.goto_why_us, name="goto_why_us"),
    url(r'directions/', views.goto_directions, name="goto_directions"),
    url(r'dash_panel/', include('dash_panel.urls'))
    # url(r'^cart_for_checkout/(?P<cart_id>\d+)/$', main_view.cart_for_checkout, name='cart_for_checkout'),

]

# if settings.DEBUG:
urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
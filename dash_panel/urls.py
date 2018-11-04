# -*- coding: utf-8 -*-

from django.conf.urls import url
from dash_panel import views as views_dash_panel
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'dash_panel'

urlpatterns = [
    url(r'^$', views_dash_panel.dash_panel_login_view, name="dash_panel_login"),
    url(r'^index/$', views_dash_panel.dash_panel_index_view, name="dash_panel_index"),
    # url(r'^check_login/$', views_dash_panel.check_login, name="dash_panel_check_login"),
    url(r'^add_user/$', views_dash_panel.add_user, name="add_user"),
    url(r'^add_portfolio_item/$', views_dash_panel.add_portfolio_item, name="add_portfolio_item"),
    url(r'^portfolio_item_details/(?P<project_id>\d+)/$', views_dash_panel.portfolio_item_details, name="portfolio_item_details"),
    url(r'^portfolio_list/$', views_dash_panel.portfolio_list, name="portfolio_list"),
    url(r'^del_fotos_from_galley/$', views_dash_panel.del_foto_from_gallery, name="del_foto_from_gallery"),
]

# if settings.DEBUG:
urlpatterns += staticfiles_urlpatterns()

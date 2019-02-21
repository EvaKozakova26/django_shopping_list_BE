from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import ItemsView

urlpatterns = [
    # ex: /app/
    #    path('', views.index, name='index'),
    # ex: /app/5/
    # Add Django site authentication urls (for login, logout, password management)
    #  path('', include('django.contrib.auth.urls')),

    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', ItemsView.as_view(), name="index"),

    path('api/items/', views.ItemsView.as_view()),
    path('api/lists/', views.ShoppingListsView.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
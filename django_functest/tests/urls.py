import django
from django.conf.urls import include, patterns, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^django_functest/', include('django_functest.urls')),
    url(r'^test_misc/', views.test_misc, name='django_functest.test_misc'),
    url(r'^list_things/', views.list_things, name='list_things'),
    url(r'^edit_thing/(?P<thing_id>.*)/', views.edit_thing, name='edit_thing'),
    url(r'^thing_cleared/(?P<thing_id>.*)/', views.thing_cleared, name='thing_cleared'),
]

if django.VERSION < (1, 9):
    urlpatterns = patterns('', *urlpatterns)

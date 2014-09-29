from django.conf.urls import patterns, include, url
from django.contrib import admin
from todoapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.todolist),
    url(r'^api/add', views.add),
    url(r'^api/delete', views.delete),
    url(r'^api/check', views.check),
)
from django.conf.urls import patterns, include, url
from apacheauth import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd120tools.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'apacheauth/login.html'},
        name='mysite_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='mysite_logout'),
    
    url(r'^accounts/change_password/$', 'password_change', {'template_name':'apacheauth/password_change.html'}, name='password_change'),
    url(r'^accounts/change_password/done/$', 'password_change_done', {'template_name':'apacheauth/password_change_done.html'}, name='password_change_done'),
)

urlpatterns += patterns('apacheauth.views',
    url(r'^$', 'index'),
    url(r'^accounts/profile/$', 'account_info'),
)


from django.conf.urls import patterns, include, url
from django.contrib import admin
import jackbot.views as v

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',v.index),
    url(r'^facebook_auth$',v.MychatbotView.as_view()),
)

from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import test.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
	url(r'^base', hello.views.base, name='base'),
	url(r'^salao', hello.views.salao, name='salao'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^test', test.views.index, name='index'),
]

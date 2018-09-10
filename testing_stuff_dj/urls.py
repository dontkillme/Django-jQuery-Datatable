from django.conf.urls import include, url, static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'testing_stuff_dj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dt_pagination.views.main_view'),
    url(r'^page/$', 'dt_pagination.views.get_part_data'), 
    url(r'^admin/', include(admin.site.urls)),
]
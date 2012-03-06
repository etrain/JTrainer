from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^q/$', 'jflashcards.views.index'),
    url(r'^q/(?P<clue_id>\d+)/$', 'jflashcards.views.clue'),
    url(r'^q/response/(?P<clue_id>\d+)/$', 'jflashcards.views.respond'),
)

from django.conf.urls import url
from basicApp import views

#for template tagging
app_name = 'basicApp'

urlpatterns=[
    url(r'^relativeUrls/$',views.relativeUrls,name='relativeUrls'),
    url(r'^other/$',views.other,name='other'),
]
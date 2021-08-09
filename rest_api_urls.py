from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^create_user$',views.create_user),
    url(r'^user_info/(?P<email_id>[\S+@\S+]+)',views.user_info),
    url(r'^get_active_users$',views.get_active_users),
    url(r'^sort_by_qualification$',views.sort_by_qualification),
    url(r'^update_an_entry/(?P<email_id>[\S+@\S+]+)',views.update_an_entry),
]


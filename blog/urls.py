from django.conf.urls import url

from .views import show_blog, get_blog, show_all_blog, show_all_blog_from_user

urlpatterns = [
    url(r'^$', show_blog),
    url(r'^(?P<blog_id>[0-9]+)', get_blog),
    url(r'^all/$',show_all_blog),
    url(r'^all/user/(?P<userId>[0-9]+)$', show_all_blog_from_user),
]

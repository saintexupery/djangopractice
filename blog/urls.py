from django.conf.urls import url

urlpatterns = [
    url(r'^blog/$', 'blog.views.post_list', name='post_list'),
    url(r'^blog/(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^blog/(?P<post_pk>\d+)/comments/new/$', 'blog.views.comment_new', name='comment_new'),
]
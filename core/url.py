from .views import PostView, CommentListView


from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^api/posts/(?P<pk>\d+)/$', PostView.as_view(), name='post-api'),
    url(r'^api/posts/comments/(?P<pk>\d+)/$', CommentListView.as_view(), name='post-api'),

]

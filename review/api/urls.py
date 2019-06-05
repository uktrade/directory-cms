from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^comments/$', views.CommentList.as_view(), name='comment_list'),
    url(r'^comments/(?P<pk>\d+)/$', views.Comment.as_view(), name='comment'),
    url(r'^comments/(?P<pk>\d+)/replies/$', views.CommentReplyList.as_view(), name='commentreply_list'),
    url(r'^comments/(?P<comment_pk>\d+)/replies/(?P<pk>\d+)/$', views.CommentReply.as_view(), name='commentreply'),
]

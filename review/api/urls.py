from django.conf.urls import url

from . import views


app_name = 'review_api'
urlpatterns = [
    url(r'^comments/$', views.CommentList.as_view(), name='comment_list'),
    url(r'^comments/(?P<pk>\d+)/$', views.Comment.as_view(), name='comment'),
    url(r'^comments/(?P<pk>\d+)/replies/$', views.CommentReplyList.as_view(), name='commentreply_list'),
    url(r'^comments/(?P<comment_pk>\d+)/replies/(?P<pk>\d+)/$', views.CommentReply.as_view(), name='commentreply'),
    url(r'^comments/(?P<pk>\d+)/resolved/$', views.CommentResolved.as_view(), name='comment_resolved'),
    url(r'^moderation/lock/$', views.ModerationLock.as_view(), name='lock'),
    url(r'^moderation/respond/$', views.ModerationRespond.as_view(), name='respond'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clear/$', views.clear),
    url(r'^status/$', views.status),
    url(r'^forum/create/$', views.createf),
    url(r'^forum/details/$', views.detailsf),
    url(r'^forum/listPosts/$', views.listpostsf),
    url(r'^forum/listThreads/$', views.listthreadsf),
    url(r'^forum/listUsers/$', views.listusersf),
    url(r'^post/create/$', views.createp ),
    url(r'^post/details/$', views.detailsp ),
    url(r'^post/list/$', views.listp ),
    url(r'^post/remove/$', views.removep ),
    url(r'^post/restore/$', views.restorep),
    url(r'^post/update/$', views.updatep ),
    url(r'^post/vote/$', views.votep),
    url(r'^user/create/$', views.createu),
    url(r'^user/details/$', views.detailsu),
    url(r'^user/follow/$', views.followu),
    url(r'^user/listFollowers/$', views.listfollowersu),
    url(r'^user/listFollowing/$', views.listfollowingu),
    url(r'^user/listPosts/$', views.listpostsu),
    url(r'^user/unfollow/$', views.unfollowu),
    url(r'^user/updateProfile/$', views.updateprofileu),
    url(r'^thread/close/$', views.closet),
    url(r'^thread/create/$', views.createt),
    url(r'^thread/details/$', views.detailst),
    url(r'^thread/list/$', views.listt),
    url(r'^thread/listPosts/$', views.listpostst),
    url(r'^thread/open/$', views.opent),
    url(r'^thread/remove/$', views.removet),
    url(r'^thread/restore/$', views.restoret),
    url(r'^thread/subscribe/', views.subscribet),
    url(r'^thread/unsubscribe/$', views.unsubscribet),
    url(r'^thread/update/$', views.updatet),
    url(r'^thread/vote/$', views.votet),
]

from rest_framework import routers
from django.conf.urls import patterns, include, url

from dis2_backend.api.school import *
from dis2_backend.api.user import *
from dis2_backend.api.group import *

router = routers.DefaultRouter()

school_urls = patterns('',
    url(r'^/(?P<pk>[0-9]+)/groups$', SchoolGroupsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/students$', SchoolStudentsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/staff$', SchoolStaffList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/rewards$', SchoolRewardsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/events$', SchoolEventsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)$', SchoolDetail.as_view()),
    url(r'^$', SchoolList.as_view())
)

user_urls = patterns('',
    url(r'^/(?P<pk>[0-9]+)/achievements$', UserAchievementList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/groups$', UserGroupsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/events$', UserEventsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/schools$', UserSchoolsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)$', UserDetail.as_view()),
    url(r'^$', UserList.as_view())
)

group_urls = patterns('',
    url(r'^/(?P<pk>[0-9]+)/events$', GroupEventsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/students$', GroupStudentsList.as_view()),
    url(r'^/(?P<pk>[0-9]+)$', GroupDetail.as_view()),
    url(r'^$', GroupList.as_view())
)

api_patterns = patterns('',
    url(r'^school', include(school_urls)),
    url(r'^user', include(user_urls)),
    url(r'^group', include(group_urls)),
    url(r'^', include(router.urls)),

)

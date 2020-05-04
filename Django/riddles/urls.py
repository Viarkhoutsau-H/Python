from django.conf.urls import url
# старые import
from django.conf.urls import re_path
from . import views
# новые import для API
from django.conf.urls import include
from riddles.api import RiddleResource, OptionResource
from tastypie.api import Api

from . import views
# api_name будет указываться в URLах
# перед resource_name из api.py
api = Api(api_name='api')
api.register(RiddleResource())
api.register(OptionResource())


app_name = 'riddles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^([0-9]+)/answer/$', views.answer, name='answer'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^password-change/', views.PasswordChangeView.as_view()),
    url(r'^([0-9]+)/post/$', views.post, name='post'),
    # отправка списка сообщений
    url(r'^([0-9]+)/msg_list/$', views.msg_list, name='msg_list'),
    url(r'^([0-9]+)/post_mark/$', views.post_mark, name='post_mark'),
    # средняя оценка
    url(r'^([0-9]+)/get_mark/$', views.get_mark, name='get_mark'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^post_riddle/$', views.post_riddle, name='post_riddle'),
    url(r'^subscribe/$', views.SubscribeView.as_view()),
    url(r'^', include(api.urls)),



]

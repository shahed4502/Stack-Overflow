from django.conf.urls import url

from . import views

app_name = 'stack'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ask_question/$', views.ask_question, name='ask_question'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/answer/$',views.answer, name='answer'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

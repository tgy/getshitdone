from django.conf.urls import url

from todo.views import tasks, board

urlpatterns = [
    url(r'^$', tasks, name='tasks'),
    url(r'^(?P<slug>[\w-]+)$', board, name='board')
]

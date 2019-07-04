from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from . import views


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    #url(r'^$', schema_view)
    re_path('^schema/', schema_view),
    re_path('^register/', views.RegisterUser.as_view(), name='register'),  # register functionality
    path('todos_list/', views.TodosList.as_view(), name="todos-list"),
    path('todo/<pk>/', views.TodosDetail.as_view(), name="todos-detail"),
    path('todo/<pk>/highlight/', views.TodoDetail.as_view(), name='todo-detail'),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('user/<pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('', views.api_root),
]


urlpatterns = format_suffix_patterns(urlpatterns)

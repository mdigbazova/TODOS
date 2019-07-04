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
]


urlpatterns = format_suffix_patterns(urlpatterns)

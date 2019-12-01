

from app2.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'data/',Test.as_view())
]

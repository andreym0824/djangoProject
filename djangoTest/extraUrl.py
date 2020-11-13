from typing import Dict, List, Any, Tuple

import os
from django.http import HttpResponse
import requests
from django.template.loader import get_template
from django.conf.urls import *
from books.views import testClass

urlpatterns = [
    url(r'^image/$', testClass.otherFormatResponse, {'fileFormat': 'image'}),
    url(r'^xml/$', testClass.otherFormatResponse, {'fileFormat': 'xml'}),
    url(r'^csv/$', testClass.otherFormatResponse, {'fileFormat': 'csv'}),
    url(r'^pdf/$', testClass.otherFormatResponse, {'fileFormat': 'pdf'}),
]
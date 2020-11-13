"""djangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from djangoTest.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from books import views

books_patterns = [
    path('books/',  views.getBooks, name='books'),
    path('publisher/', views.getPublisher, name='publishers'),
]

urlpatterns = [
    url(r'^$', current_dateTime, name='home'),
    url(r'^calcDateTime/(?P<month>\w{3})/(?P<day>\d\d)/$', calcDateTime, {'model': 'dateTime'}),
    url(r'^calcDateTime/([^/]+)/([^/]+)/$', calcDateTime, {'model': 'dateTime'}),
    url(r'^dbTest/$', fetchMysql, name='dbtest'),
    path('templateTest/', templateTest, name='templateTest'),
    url(r'^otherFileResponse/', include('djangoTest.extraUrl')),

    path('admin/', admin.site.urls, name='admin'),
]
#urlpatterns += i18n_patterns(books_patterns, 'English')
urlpatterns += books_patterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseNotFound, HttpResponseServerError

from test_app import views


def handler404(r, exception=None):
    return HttpResponseNotFound()


def handler500(r, exception=None):
    return HttpResponseServerError()


admin.autodiscover()

urlpatterns = [
    url(r'^flag_in_view', views.flag_in_view, name='flag_in_view'),
    url(r'^switch-on', views.switched_view),
    url(r'^switch-off', views.switched_off_view),
    url(r'^flag-on', views.flagged_view),
    url(r'^foo_view', views.foo_view, name='foo_view'),
    url(r'^foo_view_with_args/(?P<some_number>\d+)/', views.foo_view_with_args, name='foo_view_with_args'),
    url(r'^switched_view_with_valid_redirect',
        views.switched_view_with_valid_redirect),
    url(r'^switched_view_with_valid_url_name',
        views.switched_view_with_valid_url_name),
    url(r'^switched_view_with_args_with_valid_redirect/(?P<some_number>\d+)/',
        views.switched_view_with_args_with_valid_redirect),
    url(r'^switched_view_with_args_with_valid_url_name/(?P<some_number>\d+)/',
        views.switched_view_with_args_with_valid_url_name),
    url(r'^switched_view_with_invalid_redirect',
        views.switched_view_with_invalid_redirect),
    url(r'^flagged_view_with_valid_redirect',
        views.flagged_view_with_valid_redirect),
    url(r'^flagged_view_with_valid_url_name',
        views.flagged_view_with_valid_url_name),
    url(r'^flagged_view_with_args_with_valid_redirect/(?P<some_number>\d+)/',
        views.flagged_view_with_args_with_valid_redirect),
    url(r'^flagged_view_with_args_with_valid_url_name/(?P<some_number>\d+)/',
        views.flagged_view_with_args_with_valid_url_name),
    url(r'^flagged_view_with_invalid_redirect',
        views.flagged_view_with_invalid_redirect),
    url(r'^flag-off', views.flagged_off_view),
    url(r'^cbv/switch-on', views.SwitchedView.as_view()),
    url(r'^cbv/switch-off', views.SwitchedOffView.as_view()),
    url(r'^cbv/flag-on', views.FlaggedView.as_view()),
    url(r'^cbv/flag-off', views.FlaggedOffView.as_view()),
    url(r'^cbv/switched_view_with_valid_url_name',
        views.SwtchedViewWithValidUrlName.as_view()),
    url(r'^cbv/switched_view_with_args_with_valid_url_name/(?P<some_number>\d+)/',
        views.SwtchedViewWithArgsWithValidUrlName.as_view()),
    url(r'^cbv/switched_view_with_invalid_redirect',
        views.SwtchedViewWithInvalidRedirect.as_view()),
    url(r'^cbv/flagged_view_with_valid_url_name',
        views.FlaggedViewWithValidUrlName.as_view()),
    url(r'^cbv/flagged_view_with_args_with_valid_url_name/(?P<some_number>\d+)/',
        views.FlaggedViewWithArgsWithValidUrlName.as_view()),
    url(r'^cbv/flagged_view_with_invalid_redirect',
        views.FlaggedViewWithInvalidRedirect.as_view()),

    url(r'^', include('waffle.urls')),
    url(r'^admin/', admin.site.urls),
]

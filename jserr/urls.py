from django.conf.urls.defaults import *
urlpatterns = patterns("",
    url(r"^log/$", "jserr.views.log", name="log_js_error"),
)
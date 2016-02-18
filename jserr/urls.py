from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^log/$", "jserr.views.log", name="log_js_error"),
)

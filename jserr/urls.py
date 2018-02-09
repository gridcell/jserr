from django.conf.urls import url
import jserr.views

urlpatterns = [
    url(r"^log/$", jserr.views.log, name="log_js_error"),
]

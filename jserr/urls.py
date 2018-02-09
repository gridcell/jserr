from django.conf.urls import url

urlpatterns = ["",
    url(r"^log/$", "jserr.views.log", name="log_js_error"),
]

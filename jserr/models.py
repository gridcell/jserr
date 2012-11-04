from django.db import models


class JSErrorLog(models.Model):
    line_number = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

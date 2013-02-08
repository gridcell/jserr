from django.db import models


class JSErrorLog(models.Model):
    line_number = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField(null=True, blank=True)
    browser = models.CharField(max_length=25, null=True, blank=True)
    browser_version = models.CharField(max_length=10, null=True, blank=True)
    os = models.CharField(max_length=25, null=True, blank=True)
    cookies_enabled = models.NullBooleanField(null=True, blank=True)

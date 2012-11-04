from models import JSErrorLog
from django.http import HttpResponse


def log(request):
    try:
        JSErrorLog(
            line_number=request.GET.get('l', None),
            url=request.GET.get('u', None),
            message=request.GET.get('m', None)
        ).save()
    except:
        pass
    return HttpResponse('')

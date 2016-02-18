import ua_parser
from models import JSErrorLog
from django.http import HttpResponse


def log(request):
    try:
        ua = request.META.get('HTTP_USER_AGENT')
        if ua:
            parsed_ua = ua_parser.Parse(ua)
        else:
            parsed_ua = {}

        os = parsed_ua.get('os', {})
        user_agent = parsed_ua.get('user_agent')
        JSErrorLog(
            line_number=request.GET.get('l'),
            url=request.GET.get('u'),
            message=request.GET.get('m'),
            ip=request.META.get('REMOTE_ADDR'),
            browser=user_agent.get('family') or '',
            browser_version=user_agent.get('major') or '',
            os=os.get('family'),
            cookies_enabled=request.REQUEST.get('c')
        ).save()
    except:
        traceback.print_exc()
    return HttpResponse('')

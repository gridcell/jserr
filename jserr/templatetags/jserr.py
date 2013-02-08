from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def jserr():
    return """
    <script type="text/javascript">
        if (%s) {
            window.onerror = function(message, url, lineNumber){
                var ua = navigator.userAgent;
                var c = navigator.cookiesEnabled;
                var b = new Image();
                var q = 'm=' + message + '&u=' + url + '&l=' + lineNumber + '&ua=' + escape(ua) + '&c=' + c;
                b.src = '/jserr/log/?' + q;
                return false;
            };
        }
    </script>
    """ % ('true' if not settings.DEBUG else 'false')

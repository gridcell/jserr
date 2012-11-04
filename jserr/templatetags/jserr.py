from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def jserr():
    return """
    <script type="text/javascript">
        if (%s) {
            window.onerror = function(message, url, lineNumber){
                var b = new Image();
                var q = 'm=' + message + '&u=' + url + '&l=' + lineNumber;
                b.src = '/jserr/log/?' + q;
                return false;
            };
        }
    </script>
    """ % ('true' if not settings.DEBUG else 'false')

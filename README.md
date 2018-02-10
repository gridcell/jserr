#  JSErr

  
Django app to log javascript errors.  


##  Updates
* February 7, 2013:
    * added tracking for ip address, browser, browser version, os and if cookies are enabled
* February 10, 2018:
    * Django 1.11.x compatibility

##  Prerequisites

* PyYAML: http://pypi.python.org/pypi/PyYAML/

##  Setup  
    
+ Add jserr to apps list in your settings.py file.


    `INSTALLED_APPS = [  
    ...,  
    'jserr',  
     ...,  
    ]`  

+ Sync database.
    
    `./manage.py syncdb`

+ In your template file add jserr template tag, likely before any javascript files that you want to track.

    `....  
    {% load jserr %}  
    ...  
    {% jserr %}`  

+ Add the following to your urls.py file.
    
    `url(r'^jserr/', include('jserr.urls')),`
    
+ Done :)
  
**Note: only tracks errors when not in debug mode (DEBUG = False)**  
  
## License  

Copyright (C) 2012 by Dustin Sampson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
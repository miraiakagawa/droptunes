# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
from datetime import datetime

def hello_view(request):
    """ Simple Hello World View """
    t = loader.get_template('welcome.html')
    c = Context({
        'current_time': datetime.now(),
    })
    return HttpResponse(t.render(c))

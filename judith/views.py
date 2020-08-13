from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


from django.http import HttpResponse

class HomepageView(TemplateView):
    template_name = "about.html"

#def index(request):
#    return HttpResponse("Hello, world. This is the base of Judith's portfolio site.")

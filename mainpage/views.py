from django.shortcuts import render
from django.views import generic
from mainpage.models import Notice

def index(request):
    return render(request, "index.html")

def notice(request):
    return render(request, "notice.html")

class NoticeListView(generic.ListView):
    model = Notice
    template_name = "notice.html"

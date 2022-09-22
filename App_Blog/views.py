from django.shortcuts import render
from django.http import HttpResponse


def blog_list(request):
    return render(request, 'App_Blog/blog_list.html', context={})

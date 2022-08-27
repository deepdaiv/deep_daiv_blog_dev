from http.client import REQUEST_TIMEOUT
from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_us(request):
    return render(
        request,
        'single_pages/about_us.html'
    )

def post(request):
    return render(
        request,
        'single_pages/post.html'
    )

def paper_review(request):
    return render(
        request,
        'single_pages/paper_review.html'
    )

def wiki(request):
    return render(
        request,
        'single_pages/wiki.html'
    )

def study(request):
    return render(
        request,
        'single_pages/study.html'
    )

def event(request):
    return render(
        request,
        'single_pages/event.html'

    )


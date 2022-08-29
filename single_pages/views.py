from http.client import REQUEST_TIMEOUT
from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )
<<<<<<<<< Temporary merge branch 1

=========
>>>>>>>>> Temporary merge branch 2
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
<<<<<<<<< Temporary merge branch 1
    )

=======
    )
>>>>>>> 9f9b75a6dc3b8c39514bae184c3073e222ba0acf
=======

=========
    )
>>>>>>>>> Temporary merge branch 2

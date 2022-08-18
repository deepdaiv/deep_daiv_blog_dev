from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing),
    path('about_us/',views.about_us),
    path('post/',views.post),
    path('paper_review/',views.paper_review),
    path('wiki/',views.wiki),
    path('study/',views.study),
    path('event/',views.event),
]
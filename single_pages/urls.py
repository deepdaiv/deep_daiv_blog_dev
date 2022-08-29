from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing),
<<<<<<<<< Temporary merge branch 1
    path('',views.about_us),
    path('',views.post),
    path('',views.paper_review),
    path('',views.wiki),
    path('',views.study),
    path('',views.event),

=========
    path('about_us/',views.about_us),
    path('post/',views.post),
    path('paper_review/',views.paper_review),
    path('wiki/',views.wiki),
    path('study/',views.study),
    path('event/',views.event),
>>>>>>>>> Temporary merge branch 2
]
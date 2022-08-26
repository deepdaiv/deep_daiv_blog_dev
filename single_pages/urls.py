from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing),
<<<<<<< HEAD
    path('',views.about_us),
    path('',views.post),
    path('',views.paper_review),
    path('',views.wiki),
    path('',views.study),
    path('',views.event),

=======
    path('about_us/',views.about_us),
    path('post/',views.post),
    path('paper_review/',views.paper_review),
    path('wiki/',views.wiki),
    path('study/',views.study),
    path('event/',views.event),
>>>>>>> 9f9b75a6dc3b8c39514bae184c3073e222ba0acf
]
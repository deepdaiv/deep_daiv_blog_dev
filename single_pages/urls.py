from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing),
    path('',views.about_us),
    path('',views.post),
    path('',views.paper_review),
    path('',views.wiki),
    path('',views.study),
    path('',views.event),
]
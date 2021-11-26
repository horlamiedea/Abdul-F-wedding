from django.urls import path
from .views import *

urlpatterns = [
    path("", homeview, name="home"),
    path("couple", couple, name="couple"),
    path("rsvp", rsvp, name="rsvp"),
    path("schedule", schedule, name="schedule"),
    path("travel", travel, name="travel"),
    path("faq", faq, name="faq"),
]

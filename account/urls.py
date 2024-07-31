from django.urls import path
from .views import RegisterView, RetrieveUserView

urlpatterns = [
    path('signup', RegisterView.as_view()),
    path('user', RetrieveUserView.as_view()),
]
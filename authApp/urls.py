from django.urls import path
from .views import CustomLognView

urlpatterns = [
    path('', CustomLognView.as_view()),
    path('login/', CustomLognView.as_view())
]

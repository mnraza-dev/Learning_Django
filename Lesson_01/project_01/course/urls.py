from django.urls import path
from . import views
urlpatterns = [
     path('learnpython/', views.learn_python  ),
     path('learndj/', views.learn_django  ),
]
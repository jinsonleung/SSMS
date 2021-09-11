from django.urls import path, include
from django.conf.urls import url
from persons import views


urlpatterns = [
    path('add_person', views.add_person),
    # path('add_person_2', views.add_person_2),
    path('add_person_3', views.add_person_3),
    path('show_persons', views.show_persons),
]

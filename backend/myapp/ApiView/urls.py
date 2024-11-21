from django.urls import path
from . import views
urlpatterns = [

    path('getCards/', views.GetCards),
    path("createCard/", views.CreateCard)
]

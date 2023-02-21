from django.urls import path

from . import views

app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<title>', views.entry, name="entry"),
    path('search', views.search, name="search"),
    path('newpage', views.newpage, name="newpage"),
    path('wiki/<str:entryTitle>/edit', views.editpage, name="editpage"),
    path('random', views.random, name="random"),
]

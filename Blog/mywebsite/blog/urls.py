from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    # path("single/", views.single, name="single"),

    path("post/create", views.PostCreate.as_view(), name="post_create"),
]
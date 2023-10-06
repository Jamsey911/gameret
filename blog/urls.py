"""
Imports for the blog urls
"""
from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.PublishedPosts.as_view(), name='blog'),
    path('<slug:slug>/', views.PostExpand.as_view(), name='post_detail'),
]

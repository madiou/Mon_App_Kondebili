# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('article/<int:pk>/', views.detail_article, name='detail_article'),
    path('article/ajouter/', views.ajouter_article, name='ajouter_article'),
    path('article/<int:pk>/commenter/', views.commenter_article, name='commenter_article'),
]

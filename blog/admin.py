# blog/admin.py
from django.contrib import admin
from .models import Article, Commentaire

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication', 'est_approuve')
    list_filter = ('est_approuve', 'date_publication')
    search_fields = ('titre', 'contenu')

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('article', 'auteur', 'date_publication', 'est_approuve')
    list_filter = ('est_approuve', 'date_publication')

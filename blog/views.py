from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Commentaire
from .forms import ArticleForm, CommentaireForm
from django.contrib.auth.decorators import login_required

def liste_articles(request):
    articles = Article.objects.filter(est_approuve=True).order_by('-date_publication')
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk, est_approuve=True)
    commentaires = article.commentaires.filter(est_approuve=True)
    return render(request, 'blog/detail_article.html', {
        'article': article, 
        'commentaires': commentaires
    })

@login_required
def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'blog/ajouter_article.html', {'form': form})

@login_required
def commenter_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user
            commentaire.article = article
            commentaire.save()
            return redirect('detail_article', pk=pk)
    else:
        form = CommentaireForm()
    return render(request, 'blog/commenter_article.html', {'form': form, 'article': article})

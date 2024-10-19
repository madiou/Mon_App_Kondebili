from django.db import models

# Create your models here.
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_publication = models.DateTimeField(auto_now_add=True)
    est_approuve = models.BooleanField(default=False)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    article = models.ForeignKey(Article, related_name='commentaires', on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    est_approuve = models.BooleanField(default=False)

    def __str__(self):
        return f'Commentaire de {self.auteur} sur {self.article}'

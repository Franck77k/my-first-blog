from django.db import models# on importe le model de la base 
                           # de donnée de django

from django.utils import timezone # on importe timezone de 
#                                     # outils django 

class Post(models.Model):
    # definit le models. C'est un objet Post 
#     # est le nom del'objet . models.Model est un modèle de djago 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Autheur, ForeignKey lien vers autre model
    title = models.CharField(max_length=200)
     # CharField champ avec caracère limité 
    text = models.TextField()
    # TextField champ caractère no limit
    created_date = models.DateTimeField(default=timezone.now)
    # date création, DateTimeField  champ ou heure 
    published_date = models.DateTimeField(blank=True, null=True)
    # date publication

    def publish(self):
        # créons une fonction ou une methode publish est le nom de la fonction ou la methode 
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # methode __str__() (string) 
        return self.title
        # Renvoie du texte str 











# from django.db import models # on importe le model de la base 
#                             # de donnée de django

# # Create your models here.

# from django.utils import  timezone # on importe timezone de 
#                                     # outils django 




# class Post(models.Model): 
#     # definit le models. C'est un objet Post 
#     # est le nom del'objet . models.Model est un modèle de djago 
#     author = models.ForeignKey('auth.User') 
#     # Autheur, ForeignKey lien vers autre model
#     title = models.CharField(max_length = 200)
#     # CharField champavec carète limité 
#     text = models.TextField() 
#     # TextField champ caractère no limit
#     created_date = models.DateTimeField(default = timezone.now) 
#         # date création, DateTimeField  champ ou heure 
#     published_date = models.DateTimeField(blank = True, null = True) 
#         # date publication

    
#     def publish (self) : # créons une fonction ou une methode publish est le nom de la fonction ou la methode 
#         self.published_date = timezone.now()
#         self.save()

#     def __str__ (self) : 
#         # methode __str__() (string) 
#         return self.title 
#         # Renvoie du texte str 

from django.contrib import admin

# Register your models here.

from .models import Post


admin.site.register(Post) # Permet la visibilité  du modèle 
# dans l'interface administration en enregistrant notre modèle 
# à l'aide de admin.site.register(Post)

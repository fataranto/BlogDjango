from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name="Publicado")
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateField(auto_now=True, verbose_name="Editado el")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

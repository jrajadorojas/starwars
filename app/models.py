from django.db import models
from django.urls import reverse

class Film(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='films/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'film'
        verbose_name_plural = 'films'


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("app:film_detail",args=[self.slug])
    

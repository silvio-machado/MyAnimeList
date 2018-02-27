from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique=True)

    def __str__(self):
        return self.top_name

class Animes (models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length = 264, unique=True)
    
    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'

    def __str__(self):
        return self.name

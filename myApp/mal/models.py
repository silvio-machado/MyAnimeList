import datetime
from django.utils import timezone
from django.db import models


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
        
    def __str__(self):
        return self.top_name


class Animes (models.Model):
    JA_ASSISTI = "ja"
    QUERO_ASSISTIR = "qa"
    ESTOU_ASSISTINDO = "ea"
    STATUS_CHOICES = [
        (JA_ASSISTI, "ja assisti"),
        (QUERO_ASSISTIR, "Quero assistir"),
        (ESTOU_ASSISTINDO, "Estou assistindo"),
    ]
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    status = models.CharField(max_length =264, choices=STATUS_CHOICES, default=QUERO_ASSISTIR)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    class Meta:
        unique_together = ('topic', 'name')
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'

        
    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

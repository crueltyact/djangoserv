from django.db import models

class Review(models.Model):
    mark = models.IntegerField(verbose_name='Rate us')
    review = models.TextField(verbose_name='Review', max_length=255)

    def __str__(self):
        return self.mark
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'  
        
# Create your models here.

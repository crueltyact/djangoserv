from django.db import models

class Review(models.Model):
    mark = models.DecimalField(verbose_name='Rate us', max_length=10, max_digits=2, decimal_places = 0)
    reviewww = models.TextField(verbose_name='Review', max_length=255)

    def __str__(self):
        return str(self.mark)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'  
        
# Create your models here.

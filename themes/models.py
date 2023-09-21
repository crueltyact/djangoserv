from django.db import models
from template.models import Template

class Theme(models.Model):
    template = models.ManyToManyField(verbose_name='Theme', to=Template, related_name='themes')
    shortdesc = models.TextField(verbose_name='Theme description', max_length=255)
    amount = models.IntegerField(verbose_name='Themes amount')

    def __str__(self):
        return self.shortdesc

    class Meta:
        verbose_name = 'theme'
        verbose_name_plural = 'themes' 
        
# Create your models here.

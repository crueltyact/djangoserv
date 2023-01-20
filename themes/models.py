from django.db import models
from template.models import Template

class Theme(models.Model):
    shortdesc = models.TextField(verbose_name='Theme description', max_length=64)
    amount = models.IntegerField(verbose_name='Themes amount')
    template = models.ManyToManyField(verbose_name='Theme', to=Template, related_name='themes')

    def __str__(self):
        return self.shortdesc

    class Meta:
        verbose_name = 'theme'
        verbose_name_plural = 'themes' 
        
# Create your models here.

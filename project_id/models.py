from django.db import models
from themes.models import Theme

class MyProject(models.Model):
    name = models.CharField(verbose_name='Name', max_length=64)
    introduction = models.TextField(verbose_name='Introduction', max_length=255)
    questions = models.TextField(verbose_name='Question', max_length=255)
    ending = models.TextField(verbose_name='Ending', max_length=255) 
    theme = models.ManyToManyField(verbose_name='Project theme', to=Theme, related_name='project_id')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'MyProject'
        verbose_name_plural = 'MyProjects'  

# Create your models here.

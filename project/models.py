from django.db import models
from project_id.models import MyProject


class Project(models.Model):
    project_id = models.ManyToManyField(verbose_name='Projects', to=MyProject, related_name='Project')
    project_name = models.CharField(verbose_name='Name', max_length=255)
    created_date = models.DateField(verbose_name='Created')
    updated_date = models.DateTimeField(verbose_name='Updated')
    themes = models.TextField(verbose_name='Themes', max_length=255)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects' 
        
# Create your models here.

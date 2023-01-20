from django.db import models

class MyProject(models.Model):
    name = models.CharField(verbose_name='Name', max_length=64)
    introduction = models.TextField(verbose_name='Introduction', max_length=255)
    questions = models.TextField(verbose_name='Question', max_length=64)
    ending = models.TextField(verbose_name='Ending', max_length=255)    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'MyProject'
        verbose_name_plural = 'MyProjects'  

# Create your models here.

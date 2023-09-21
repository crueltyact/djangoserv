from django.db import models


class Template(models.Model):
    name = models.CharField(verbose_name='Template name', max_length=255)
    desc = models.TextField(verbose_name='Description', max_length=255)
    cover = models.ImageField(verbose_name='Cover', upload_to='users/photos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'template'
        verbose_name_plural = 'templates'  
from django.db import models

from mailing import constants


# Create your models here.


class Blog(models.Model):

    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='сщдержимое статьи')
    picture = models.ImageField(upload_to='blog/', verbose_name='изображение', **constants.NULLABLE)
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    date_publish = models.DateField(verbose_name='дата публикации', auto_now=True)

    def __str__(self):
        return f'{self.title} {self.content} {self.date_publish}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

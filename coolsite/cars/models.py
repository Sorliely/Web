from django.db import models

class Cars(models.Model):
    """БД истории"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True) #время создание записи
    time_update = models.DateTimeField(auto_now=True) #время обновления
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


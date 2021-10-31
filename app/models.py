from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    content = models.TextField('本文')
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

from django.db import models


# Новостные статьи для нашей страницы со списком всех новостей
class New(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True, # названия статей не должны повторяться
    )
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',  # все новости в категории будут доступны через поле news
    )

    def __str__(self):
        return f'{self.title.title()}: {self.dateCreation}: {self.text[:20]}'

# Категория, к которой будет привязываться новость
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name.title()



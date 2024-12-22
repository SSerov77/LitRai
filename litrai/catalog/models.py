from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    name = models.CharField('Имя', max_length=200)
    biography = models.TextField('Биография', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    BOOK_TYPE_CHOICES = [
        ('P', 'Печатная'),
        ('E', 'Электронная'),
        ('A', 'Аудиокнига'),
    ]

    title = models.CharField('Название', max_length=250)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        null=True,
        related_name='books'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        verbose_name='Автор',
        null=True,
        related_name='books'
    )
    description = models.TextField('Описание', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    publish_date = models.DateField('Дата публикации')
    book_type = models.CharField('Формат', max_length=1, choices=BOOK_TYPE_CHOICES)
    cover_image = models.ImageField('Изображение', upload_to='book_covers/', blank=True, null=True)
    is_available = models.BooleanField('В наличии', default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
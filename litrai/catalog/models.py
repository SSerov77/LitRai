from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    BOOK_TYPE_CHOICES = [
        ('P', 'Печатная'),
        ('E', 'Электронная'),
        ('A', 'Аудиокнига'),
    ]

    title = models.CharField(max_length=250)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publish_date = models.DateField()
    book_type = models.CharField(max_length=1, choices=BOOK_TYPE_CHOICES)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
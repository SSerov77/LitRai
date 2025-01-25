from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from catalog.models import Category, Author, Book


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Художественная литература',
            description='Книги, которые представляют собой художественные произведения.'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Художественная литература')
        self.assertEqual(self.category.description, 'Книги, которые представляют собой художественные произведения.')
        self.assertEqual(str(self.category), 'Художественная литература')

    def test_category_verbose_name(self):
        self.assertEqual(Category._meta.verbose_name, 'Категория')

    def test_category_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, 'Категории')


class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='Лев Толстой',
            biography='Русский писатель, один из величайших писателей мира.'
        )

    def test_author_creation(self):
        self.assertEqual(self.author.name, 'Лев Толстой')
        self.assertEqual(self.author.biography, 'Русский писатель, один из величайших писателей мира.')
        self.assertEqual(str(self.author), 'Лев Толстой')

    def test_author_verbose_name(self):
        self.assertEqual(Author._meta.verbose_name, 'Автор')

    def test_author_verbose_name_plural(self):
        self.assertEqual(Author._meta.verbose_name_plural, 'Авторы')


from datetime import date  # Импортируем модуль date из datetime


class BookModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Художественная литература',
            description='Книги, которые представляют собой художественные произведения.'
        )
        self.author = Author.objects.create(
            name='Лев Толстой',
            biography='Русский писатель, один из величайших писателей мира.'
        )
        self.book = Book.objects.create(
            title='Война и мир',
            category=self.category,
            author=self.author,
            description='Роман-эпопея, описывающий события войны против Наполеона.',
            price=500.00,
            publish_date=date(1869, 1, 1),  # Используем объект date
            book_type='P',
            cover_image=SimpleUploadedFile("test_image.jpg", b"file_content"),
            is_available=True
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Война и мир')
        self.assertEqual(self.book.category, self.category)
        self.assertEqual(self.book.author, self.author)
        self.assertEqual(self.book.description, 'Роман-эпопея, описывающий события войны против Наполеона.')
        self.assertEqual(self.book.price, 500.00)
        self.assertEqual(self.book.publish_date, date(1869, 1, 1))  # Сравниваем с объектом date
        self.assertEqual(self.book.book_type, 'P')
        self.assertTrue(self.book.cover_image)
        self.assertTrue(self.book.is_available)
        self.assertEqual(str(self.book), 'Война и мир')


class CatalogURLTests(TestCase):
    def setUp(self):
        # Создаем тестовую книгу
        self.book = Book.objects.create(
            title='Тестовая книга',
            price=100.00,
            publish_date='2023-01-01',
            book_type='P',
            is_available=True
        )
        self.client = Client()

    def test_catalog_url(self):
        # Проверяем, что URL каталога возвращает статус 200
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)


class CatalogViewsTests(TestCase):
    def setUp(self):
        # Создаем клиент для отправки запросов
        self.client = Client()

    def test_index_view(self):
        # Проверяем, что представление index возвращает правильный ответ
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)  # Проверяем статус код
        self.assertEqual(response.content.decode(), "Welcome to the Catalog")  # Проверяем содержимое
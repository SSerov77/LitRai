from django.shortcuts import render

from catalog.models import Book

def index(request):
    book_sections = {
        'ЛУЧШИЕ ИЗ ЛУЧШИХ': Book.objects.filter(is_available=True)[:5],  # Пример фильтрации
        'НОВИНКИ ЛИТЕРАТУРЫ': Book.objects.order_by('-publish_date')[:5], # Новые публикации
        'СКОРО В ПРОДАЖЕ': Book.objects.filter(is_available=False)[:5]  # Нет в наличии
    }
    
    context = {
        'book_sections': book_sections
    }
    return render(request, 'home/home.html', context)
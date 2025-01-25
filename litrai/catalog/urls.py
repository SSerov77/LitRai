from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalog'),  # Каталога
    # path('<int:book_id>/', views.detail, name='book_detail'),  # Страница конкретной книги
]
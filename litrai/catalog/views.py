from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Catalog")

# def detail(request, book_id):
#     return HttpResponse(f"Details of Book ID: {book_id}")
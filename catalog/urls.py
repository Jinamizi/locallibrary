from django.urls import path
from . import views

urlpatterns = [
    #name - a unique identifier for a url mapping. use the name to "reverse" the mapper, 
    # i.e to dynamically create a URL that points to the resource that the mapper is designed to handle
    path('', views.index, name='index'), 
    #path('books/', views.get_books, name="books"),
    path('books/', views.BookListView.as_view(), name='books'),
    path('test/', views.test, name="test"),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

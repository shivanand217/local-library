from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),    
]

# Borrowed Books urls
urlpatterns += [
    path('mybooks/', views.LoanedBookByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

# Add URLConf  for librarian to renew a book
urlpatterns += [
    path('book/<uuid:pk>/renew/', )
]



from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # name is used to reverse the mapper
    path('', views.index, name='index'),
    # path('books/', views.book_list_view, name='books'),
    # path('book/<int:pk>', views.book_detail_view, name='book-detail'),
    # or, re_path(r'^book/(?P<pk>\d+)', views.BookDetailView.as_view(),name='book-detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_list),
    path('books/<int:pk>/', views.book_detail),
    path('books/<int:pk>/upload-cover/', views.upload_cover),
]

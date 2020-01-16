from django.urls import path

from .views import BookDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('post/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('', BookListView.as_view(), name='home'),
    path('new/', BookCreateView.as_view(), name='new'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
]

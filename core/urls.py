from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('series/', views.SeriesListView.as_view(), name='series'),
    path('series/<int:pk>', views.SeriesDetailView.as_view(), name='series-detail'),
    
]

urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]

urlpatterns += [
    path('chapter/create/', views.ChapterCreate.as_view(), name='chapter-create'),
    path('chapter/<int:pk>/update/', views.ChapterUpdate.as_view(), name='chapter-update'),
    path('chapter/<int:pk>/delete/', views.ChapterDelete.as_view(), name='chapter-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
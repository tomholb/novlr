from django.contrib import admin
from .models import Author, Genre, Book, Chapter, Series, NarrativeForm

# Register your models here.
admin.site.register(Series)
#admin.site.register(Book)
#admin.site.register(Chapter)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(NarrativeForm)

#Register the Admin Classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'status')
    
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'number', 'title', 'status')
    list_filter = ['status']
    
@admin.register(Author)    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
from django.db import models
from django.urls import reverse #used to generate URLs by reversing the url pattern
from ckeditor.fields import RichTextField

# Create your models here.
class NarrativeForm(models.Model):
    type = models.CharField(max_length=50, help_text='Fiction or Non Fiction')
    
    def __str__(self):
        """String representing the object"""
        return self.type

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text='Enter  book genre')

    
    def __str__(self):
        """String for representing the Model Object"""
        return self.name
        
class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)
    BOOK_STATUS = (
        ('d', 'Draft'),
        ('a', 'Alpha'),
        ('b', 'Beta'),
        ('f', 'Final'),
    )
    status = models.CharField(
        max_length=1,
        choices=BOOK_STATUS,
        blank=True,
        default='d',
        help_text='Chapter Status',
    )
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    narrative = models.ForeignKey('NarrativeForm', on_delete=models.SET_NULL, help_text='Select if this is a work of fiction or non-fiction.', null=True)
    # Foreign Key for Author, which is a one to many relationship (one author to many books)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    series = models.ForeignKey('Series', on_delete=models.SET_NULL, null=True, blank=True)
    series_number = models.IntegerField(default=1, blank=True, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    
    
    
    
    def __str__(self):
        """String representing the Model Object"""
        return self.title
       
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book"""
        return reverse('book-detail', args=[str(self.id)])
        
        
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'
    
class Chapter(models.Model):
    """Model representing a specific chapter in a book"""
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    number = models.IntegerField(default=1, blank=False, null=False)
    title = models.CharField(max_length=200)
    writing_status = (
        ('d', 'Draft'),
        ('a', 'Alpha'),
        ('b', 'Beta'),
        ('f', 'Final'),
    )
    body = RichTextField(config_name='awesome_ckeditor')
    
    status = models.CharField(
        max_length=1,
        choices=writing_status,
        blank=True,
        default='d',
        help_text='Chapter Status',
    )
    
    class Meta:
        ordering = ['number']
        
    def __str__(self):
        """String for representing the model object"""
        return f'{self.id} ({self.book.title})'
        
    def word_count(self):
        count = len(self.body.split())
        
        return count
        
class Author(models.Model):
    """Model representing the author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['last_name','first_name']
        
    def get_absolute_url(self):
        """Returns the URL to access the author instance"""
        return reverse('author-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the model object"""
        return f'{self.last_name}, {self.first_name}'
        
class Series(models.Model):
    """Model representing the author"""
    title = models.CharField(max_length=100)
    
           
    def get_absolute_url(self):
        """Returns the URL to access the author instance"""
        return reverse('series-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the model object"""
        return f'{self.title}'
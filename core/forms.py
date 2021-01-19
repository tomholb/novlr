from django.forms import ModelForm
from core.models import Book, Series, Chapter

class NewBookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
from django import forms
from books.models import Books_catlog,BookReview

class add_book_form(forms.ModelForm):
    class Meta:
        model = Books_catlog
        fields = ['title', 'author', 'genere', 'book_image','avialable_free', 'avialable_paid','description', 'additional']
        
    
class add_review(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['review_text']
        
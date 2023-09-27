from django.shortcuts import render,redirect
from . forms import add_book_form,add_review
import datetime
from django.http import HttpResponse
from . models import Books_catlog,BookReview


def index(request):
    books = Books_catlog.objects.all()
    return render(request, 'books/index.html', {'book':books})
    
def add_book(request): 
    if request.method == 'POST':
        form = add_book_form(request.POST, request.FILES)
        if form.is_valid():
            addbook = form.save(commit=False)
            addbook.publication_date = datetime.date.day
            
            addbook.save()
            return redirect('index')
        else:
            return redirect('add_book')
    else:
        form = add_book_form()
        return render(request, 'books/add_book.html', {'form':form})
    
def search_books(request):
    if request.method == 'POST':
    
        query = request.POST.get('book')  # Get the search query from the request
    if query:
        # Perform a database query to search for books by name or author
        search_results = Books_catlog.objects.filter(title__icontains=query) | Books_catlog.objects.filter(author__icontains=query)
        
        return render(request, 'books/showbook.html', {'search_results': search_results,})
        
    else:
        search_results = []
        
    return redirect('index') 
#

def showbook(request, pk):
    book_details = Books_catlog.objects.get(book_id = pk)
    return render(request, 'books/detailed.html', {'book':book_details})

def write_review(request, pk):
    book_review = Books_catlog.objects.get(book_id = pk)
    if request.method == 'POST':
        form = add_review(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            #review.review_of = book_review.title
            review.reviewed_at = datetime.date.day
            review.reviewer = request.user
            if BookReview.objects.filter(review_text =None ):
                book_review.review_of = review.review_text
            else:
                book_review.review_of += review.review_text
            book_review.save(update_fields=['review_of'])
            review.save()
            return HttpResponse('added')
        else:
            return redirect('write-review')
    else:
        form = add_review()
        return render(request, 'books/review.html', {'form':form})
    
def show_review(request, pk):
    review = BookReview.objects.get(review_id=pk)
    return render(request, 'books/detailed.html', {'review':review})
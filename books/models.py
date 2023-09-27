import uuid
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class Books_catlog(models.Model):
    BOOK_GENERE = {
        ('FICTION', 'fiction'),
        ('NON-FICTION', 'non-fictinonon'),
        ('LITERATURE', 'literature'),
        ('TRADITIONAL-LITERATURE', 'trafitional'),
        ('OTHER', 'other')
    }
    book_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genere = models.CharField(max_length=255, choices=BOOK_GENERE, null=False)
    description = models.TextField()
    book_image = models.ImageField(upload_to='booksimg/', null=True, blank=True)
    avialable_free = models.BooleanField(default=True)
    avialable_paid = models.BooleanField(default=False)
    publication_date = models.DateField(auto_now_add=True)
    additional = models.TextField(null=True, blank=True)
    review_of = models.TextField(max_length=255, null=True, blank=True) 


class BookReview(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4)
    review_for_book = models.ManyToManyField(Books_catlog, related_name='bookreview', blank=True)
    review_text = models.TextField(max_length=555, unique=True)
    reviewed_at = models.DateField(auto_now_add=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

        
# Generated by Django 4.2.5 on 2023-09-27 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books_catlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genere', models.CharField(choices=[('OTHER', 'other'), ('TRADITIONAL-LITERATURE', 'trafitional'), ('LITERATURE', 'literature'), ('NON-FICTION', 'non-fictinonon'), ('FICTION', 'fiction')], max_length=255)),
                ('description', models.TextField()),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='booksimg/')),
                ('avialable_free', models.BooleanField(default=True)),
                ('avialable_paid', models.BooleanField(default=False)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('additional', models.TextField(blank=True, null=True)),
                ('review_of', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.UUIDField(default=uuid.uuid4)),
                ('review_text', models.TextField(max_length=555, unique=True)),
                ('reviewed_at', models.DateField(auto_now_add=True)),
                ('review_for_book', models.ManyToManyField(blank=True, related_name='bookreview', to='books.books_catlog')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
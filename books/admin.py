from django.contrib import admin
from books.models import Book
from books.models import Publisher
from books.models import Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
    odering = '-publication_date'
    search_fields = ['title']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'website')
    list_filter = ('name', 'city')
    odering = '-name'
    search_fields = ['name']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('salutation', 'first_name', 'last_name', 'email', 'headshot')
    list_filter = ('first_name', 'last_name',  'email')
    list_editable = ('first_name', 'last_name',  'email')
    list_display_links = ['salutation']
    ordering = ['salutation', 'first_name', 'last_name']
    search_fields = ['salutation', 'first_name', 'last_name',  'email']


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)

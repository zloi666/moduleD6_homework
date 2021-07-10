from django.contrib import admin

from library.models import Book, Author, Publisher, Friend, FriendBook

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    fields = ('ISBN', 'image', 'publisher', 'title', 'description', 'year_release', 'author', 'price', 'copy_count')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass


@admin.register(FriendBook)
class FriendBookAdmin(admin.ModelAdmin):
    pass
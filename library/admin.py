from django.contrib import admin
from .models import Book, Member, BorrowRecord


# Register your models here.



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available_copies', 'published_date')
    search_fields = ('title', 'author')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'membership_date')
    search_fields = ('name',)


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('member', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date',)

from django.shortcuts import render,redirect,get_object_or_404, redirect
from django.contrib import messages
from .models import Book,BorrowRecord
from .forms import BookForm
from .models import Member
from django.core.paginator import Paginator
from django.contrib import messages
import datetime


# Create your views here.
# List view for all books
def home(request):
    return render(request, 'home.html')  

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def book_create(request):        
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  
            form = BookForm()
    else:
        form = BookForm() 

    return render(request, 'book_create.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(request, 'Book has been deleted successfully.')
    return redirect('book_list')


def book_edit(request, pk):  
    book = get_object_or_404(Book, id=pk)  
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})




def member_list(request):
    search_query = request.GET.get('search', '')
    members = Member.objects.filter(name__icontains=search_query)

    paginator = Paginator(members, 10)  # Display 10 members per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query
    }
    return render(request, 'member_list.html', context)



def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'member_detail.html', {'member': member})

from django.shortcuts import render, redirect
from .forms import MemberForm

def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # After saving, redirect to the member list page
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})


# views.py


def borrow_book(request):
    if request.method == "POST":
        member_id = request.POST.get("member")
        book_id = request.POST.get("book")
        borrow_date = request.POST.get("borrow_date")

        member = get_object_or_404(Member, id=member_id)
        book = get_object_or_404(Book, id=book_id)

        # Check if the book is available
        if book.available_copies > 0:
            # Create a new BorrowRecord
            BorrowRecord.objects.create(
                member=member,
                book=book,
                borrow_date=borrow_date
            )
            # Decrease available copies
            book.available_copies -= 1
            book.save()
            messages.success(request, "Book borrowed successfully!")
        else:
            messages.error(request, "No copies available for this book.")

        return redirect('borrow_book')
    
    # Load available members and books
    members = Member.objects.all()
    books = Book.objects.filter(available_copies__gt=0)

    return render(request, 'borrow_book.html', {'members': members, 'books': books})




def borrow_list(request):
    borrow_records = BorrowRecord.objects.all()
    return render(request, 'borrow_list.html', {'borrow_records': borrow_records})







    
    
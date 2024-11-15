from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date', 'available_copies']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title', 'style': 'width: 300px;'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name', 'style': 'width: 300px;'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN', 'style': 'width: 300px;'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date', 'style': 'width: 300px;'}),
            'available_copies': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of available copies', 'style': 'width: 300px;'}),
        }
from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'membership_date']

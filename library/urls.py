from django.urls import path
from library import views

urlpatterns = [
    path('',views.home, name='home'),
    # path('',views.library_system, name='library_system'),
    path('book_list/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),

    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),  # Edit

     path('books/<int:pk>/', views.book_detail, name='book_detail'),
     path('books_create/', views.book_create, name='book_create'),
     path('members/', views.member_list, name='member_list'),
    path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('add_member/', views.add_member, name='add_member'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),
     path('borrow_list/', views.borrow_list, name='borrow_list'),

    

    
]
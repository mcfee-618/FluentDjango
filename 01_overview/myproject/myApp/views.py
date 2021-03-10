from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from myApp.models import Book


def index(request):
    return HttpResponse("Hello, world!")


def detail_book(request):
    book_list = Book.objects.order_by('pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'detail.html', context)


def add_book(request):
    if request.method != 'POST':
        return render(request, 'add.html')
    temp_name = request.POST['name']
    temp_author = request.POST['author']
    temp_pub_house = request.POST['pub_house']
    temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    temp_book.save()
    return redirect(reverse('detail'))

def delete_book(request,name):
    book_list = Book.objects.all()
    for book in book_list:
        if book.name == name:
            book.delete()
            return redirect(reverse('detail'))
    return HttpResponse("name not found")




def edit_book(request):
    pass

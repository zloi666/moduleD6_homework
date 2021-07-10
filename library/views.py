from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect

from library.models import Book, Author, Publisher, Friend, FriendBook
from library.forms import AuthorForm, FriendForm

def books_list(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    data = {
        "books": books
    }
    return HttpResponse(template.render(data, request))


def index(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    data = {"title": "мою библиотеку",
            "books": books
            }

    return HttpResponse(template.render(data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def publisher(request):
    template = loader.get_template("publisher.html")
    publishers = Publisher.objects.all()
    data = {
        "publishers": publishers
    }
    return HttpResponse(template.render(data, request))


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('library:author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'


def authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)

    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
                return HttpResponseRedirect(reverse_lazy('library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')

    return render(request, 'manage_authors.html', {'author_formset': author_formset})


class FriendList(ListView):
    model = Friend
    template_name = 'friends_list.html'


class FriendEdit(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('library:friend_list')
    template_name = 'friend_edit.html'


class FriendBookList(ListView):
    model = FriendBook
    template_name = 'friend_book_list.html'

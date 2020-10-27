from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
from .models import Word, comment


def user_login(request):

    return render(request, 'account/login.html',)


def home(request):
    return render(request, 'home.html')


def add(request):
    if request.method == 'GET':
        search_query = request.GET.get("add_box", None)
        print(search_query, 'fk')
        if search_query is not None:
            try:
                word = Word(title=search_query)
                word.save()
                return render(request, 'search.html', {'var': search_query})
            except:

                return render(request, 'onlysearch.html', {'var': search_query})

    if request.method == 'POST':
        content = request.POST.get("contentadd", None)
        search_query = request.GET.get("add_box", None)

        print(content, 'content', search_query)
        if content is not None and search_query is not None:
            searchword = get_object_or_404(Word, title=search_query)
            meaning = comment(word=searchword, body=content)
            meaning.save()
            return render(request, 'search.html', {'var': search_query})
    return render(request, 'search.html', )


def search(request):
    if request.method == 'POST':
        searchword = request.POST.get("search_box", None)
        all_posts= comment.objects.raw("Select * from account_comment  WHERE word_id='"+str(searchword)+"'",)

        return render(request, 'onlysearch.html', {'var': searchword, 'all_posts': all_posts})

    return render(request, 'onlysearch.html', )

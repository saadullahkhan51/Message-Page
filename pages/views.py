from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.urls import reverse

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'all_posts'

def new_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save()
        return redirect('index')
    return render(request, 'pages/new.html', {'form' : form})
            

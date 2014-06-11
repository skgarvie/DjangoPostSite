from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms

from posts.models import Post, Form
# Create your views here.
class DetailView(generic.ListView):
	model = Post
	template_name='posts/detail.html'

def index(request):
    posts_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'posts/index.html', {"posts": posts})

def viewPosts(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	context = {'latest_post_list': latest_post_list}
	return render(request, 'posts/viewPosts.html', context)

def viewComments(request, post_id):
	post = Post.objects.get(pk=post_id)
	# latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	# return render(request, 'posts/viewComments.html', {'post': post})
	context = {'post': post}
	return render(request, 'posts/viewComments.html', context)
	# return HttpResponse("You're looking at the results of poll %s." % post_id)


def listing(request):
    posts_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'posts/viewPosts.html', {"posts": posts})
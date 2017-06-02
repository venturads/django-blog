import datetime
from django import template
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from .models import Author, Tag, Category, Post

def index(request):
    return HttpResponse("Hello Django")

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {
        'now': now, 
        'template_name': 'blog/nav.html',
        'footer_name': 'blog/footer.html', }
        )
        
# view function to display a list of posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'template_name': 'blog/nav.html',
        'footer_name': 'blog/footer.html', }
        ) 
    
# view function to display a single post
def post_detail(request, pk):    
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'template_name': 'blog/nav.html',
        'footer_name': 'blog/footer.html', }
        )
        
def contact_page(request):
    return render(request, 'blog/contact_page.html', {
        'template_name': 'blog/nav.html',
        'footer_name': 'blog/footer.html', }
        )
        
def about_page(request):
    return render(request, 'blog/about_page.html', {
        'template_name': 'blog/nav.html',
        'footer_name': 'blog/footer.html', }
        )
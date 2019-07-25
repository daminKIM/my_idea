from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from . models import Post

# Create your views here.

def post(request) :
    posts = Post.objects
    post_list=Post.objects.all()  #블로그 모든 글들을 대상으로
    paginator = Paginator(post_list, 6)  #블로그 객체 여섯개를 한 페이지로 자르기
    page = request.GET.get('page')   #request된 페이지가 뭔지를 알아내고  (request페이지를 변수에 담아냄)
    posts_2 = paginator.get_page(page)
    return render(request, 'post.html', {'posts' : posts, 'posts_2' : posts_2})

def posting(request) :
    return render(request, 'posting.html')

def create(request) :
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/post/post/')

def detail(request, post_id) :
    post_detail = get_object_or_404(Post, pk = post_id) 
    return render(request, 'detail.html', {'post' : post_detail})
import uuid
from django.shortcuts import render, get_object_or_404
from .models import PageVisit, Post

def blog_home(request):
    posts = Post.objects.filter(active=True)
    return render(request, 'blog/blog_home.html', {'posts': posts})

def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug, active=True)
    session_id = request.COOKIES.get('session_id')

    # Проверяем, был ли уже просмотр данной страницы в текущей сессии
    if not PageVisit.objects.filter(page_id=post.id, session_id=session_id).exists():
        # Создаем новую запись PageVisit
        page_visit = PageVisit(page_id=post.id, session_id=session_id)
        page_visit.save()
        post.views += 1
        post.save()

    return render(request, 'blog/blog_post.html', {'post': post, 'session_id': session_id})


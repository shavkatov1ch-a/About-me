from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import CommentForm
from .models import *
from contact.form import ContactForm


def hom_resume(request):
    post = AboutResume.objects.all()
    context = {'post': post}
    return render(request, 'index.html', context)

def article_detail_page(request, pk):
    post = get_object_or_404(Article, pk=pk)
    detail = get_object_or_404(Blog, pk=pk)
    tags = request.GET.get('tags')
    comment = Comment.objects.filter(article_id=pk).order_by('-id')
    if tags:
        post = post.tags.filter(tags__name=tags)
    if request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = post
            comment.save()
            return redirect(f"/detail/{post.id}")
    else:
        form = CommentForm()
    context = {'articles': post,
               'details': detail,
               'form': form,
               'comments': comment,
               'tags': tags}
    return render(request, 'single.html', context)

def home_page(request):
    article = Article.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(article, 3)
    page = request.GET.get('page')
    proj = Projects.objects.all()
    post = About.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    blog = Blog.objects.all()
    skill = Skills.objects.all()
    award = Awards.objects.all()
    art = Service.objects.all()
    form = ContactForm(request.POST)
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = ContactForm()
    context = {
        'educations': education,
        'experience': experience,
        'skills': skill,
        'awards': award,
        'posts': post,
        'blog': blog,
        'arts': art,
        'form': form,
        'articles': article,
        'tags': tags,
        'proj': proj

    }
    return render(request, 'index.html', context)



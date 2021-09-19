from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from .forms import PostForm, UpdateForm
from .models import Post


def post_list(request, template_name='home.html'):
    posts = Post.objects.all()
    data = {'data': posts}
    return render(request, template_name, data)


def post_detail(request, slug, template_name='post_detail.html'):
    single_post = Post.objects.get(slug=slug)
    context = {'data': single_post}
    return render(request, template_name, context)


def post_create(request, template_name='post_new.html'):
    context = {}
    form = PostForm(request.POST or None)
    if form.is_valid:
        form.save()
        return
    context['form'] = form
    return redirect(request, template_name, context)


def post_update(request, pk, template_name='post_edit.html'):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            titl = form.cleaned_data['title']
            bod = form.cleaned_data['body']
            Post.update_post(post.id, titl, bod)
            return redirect(post_detail, post.slug)

    forms = UpdateForm()
    contex = {'form': forms, 'post': post}
    return render(request, template_name, contex)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    Post.delete_post(post.id)
    return redirect(post_list)


def confirm_delete(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_delete.html', context={'post': post})

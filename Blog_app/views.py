from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from taggit.models import Tag

from .forms import PostForm, UpdateForm, CommentForm, SearchForm
from .models import Post, Comment


def post_list(request, tag_slug=None, template_name='blog/post/home.html'):
    list_post = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        list_post = list_post.filter(tags__in=[tag])
    paginator = Paginator(list_post, 3)  # display 3 posts on each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    data = {'data': posts, 'page': page, 'tag': tag}
    return render(request, template_name, data)


def post_detail(request, slug, template_name='blog/post/post_detail.html'):
    single_post = Post.objects.get(slug=slug)
    comments = single_post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)  # model instance created but not saved to the DB
            new_comment.post = single_post
            new_comment.save()
    else:
        comment_form = CommentForm()
        # list similar tags
    post_tags_ids = single_post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids) \
        .exclude(id=single_post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')) \
                        .order_by('same_tags', '-publish')[:4]
    context = {'data': single_post,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form,
               'similar_posts': similar_posts}
    return render(request, template_name, context)


def post_create(request, template_name='blog/post/post_new.html'):
    context = {}
    form = PostForm(request.POST or None)
    if form.is_valid:
        form.save()
        return
    context['form'] = form
    return redirect(request, template_name, context)


def post_update(request, pk, template_name='blog/post/post_edit.html'):
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
    # return HttpResponse(request,"you reached here")
    return render(request, template_name, contex)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    Post.delete_post(post.id)
    return redirect(post_list)


def confirm_delete(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post/post_delete.html', context={'post': post})


def post_search(request, template_name='blog/post/search.html'):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            # Ordinary search
            # results = Post.objects.filter(status='published'). \
            #     annotate(search=SearchVector('title', 'body'), ). \
            #     filter(search=query)
            # search_vector=SearchVector('title','body')

            # Search with stemming and ranking functionality
            search_vector = SearchVector('title', weight='A') + \
                            SearchVector('title', weight='B')
            search_query = SearchQuery(query)
            results = Post.objects.filter(status='published'). \
                annotate(search=search_vector,
                         rank=SearchRank(search_vector, search_query)
                         ).filter(search=search_query).order_by('-rank')

            # Triagram similarity search
            # results = Post.objects.filter(status='published').annotate(
            #     similarity=TrigramSimilarity('title', query),
            # ).filter(similarity__gt=0.3).order_by('-similarity')
    context = {'form': form, 'query': query, 'results': results}
    return render(request, template_name, context)

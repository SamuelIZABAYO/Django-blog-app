import markdown
from django import template
from django.utils.safestring import mark_safe

from ..models import Post

register = template.Library()


@register.simple_tag(name='total_posts')
def total_posts():
    return Post.objects.filter(status='published').count()


@register.inclusion_tag('blog/post/latest_posts.html')
def get_recent_posts(num=5):
    latest_posts = Post.objects.filter(status='published').order_by('-publish')[:num]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.filter(status='published').annotate(
        total_comments=count('comments')
    ).order_by('total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

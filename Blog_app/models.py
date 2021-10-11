from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from taggit.models import Tag


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Publish'),
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    slug = AutoSlugField(populate_from='title',
                         unique_with='publish',
                         unique=True,
                         db_index=True,
                         max_length=200
                         # editable=False,
                         )
    tags = TaggableManager()

    @classmethod
    def update_post(cls, post_id, title, body):
        cls.objects.filter(id=post_id).update(title=title, body=body)

    @classmethod
    def delete_post(cls, post_id):
        cls.objects.get(id=post_id).delete()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post:post_detail',
    #                    # kwargs={'slug': self.slug})
    #                    args=[
    #                        self.publish.year,
    #                        self.publish.month,
    #                        self.publish.day,
    #                        self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "Comment by {} on {}".format(self.name, self.post)

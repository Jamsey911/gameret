"""
Imports for blog views
"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post
from .forms import CommentForm


class PublishedPosts(generic.ListView):
    """
    VIew to show a list of paginated published blogs
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'blog.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):
        """
        This view renders the blog page and also all published posts
        """
        posts = Post.objects.all()
        paginator = Paginator(Post.objects.all(), 4)
        page = request.GET.get('page')
        postings = paginator.get_page(page)

        context = {
            'posts': posts,
            'postings': postings
        }

        return render(
            request,
            'blog/blog.html',
            context
        )


class PostExpand(View):
    """
    View for the post to be read by the user
    """
    def get(self, request, slug, *args, **kwargs):
        """
        View for the post to be read by the user
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(
            approved=True).order_by('-created_date')

        context = {
            'post': post,
            'comments': comments,
            'commented': False,
            'comment_form': CommentForm()
        }

        return render(
            request,
            'blog/blog_detail.html',
            context
        )

    def post(self, request, slug, *args, **kwargs):
        """
        View for the post to be read by the user
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(
            queryset,
            slug=slug
        )
        comments = post.comments.filter(
            approved=True).order_by('-created_date')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Comment pending approval')
        else:
            comment_form = CommentForm()
            messages.error(request, 'Please try again')

        return render(
            request, 'blog/blog_detail.html',
            {'post': post,
             'comments': comments,
             'commented': True,
             'comment_form': CommentForm()
             }
        )

from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Comment  # , EmailMessage
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm, EncryptForm, DecryptForm, EmailMessageForm
from django.contrib.auth.decorators import login_required
import inspect


def lineno():
    """Returns the current line number in our program.
    lineno() is a function to make it easy to grab the line
    number that we're on. Danny Yoo (dyoo@hkn.eecs.berkeley.edu)"""
    return inspect.currentframe().f_back.f_lineno


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # import pdb; pdb.set_trace()
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    print(lineno(), 'request.method =', request.method)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.last_update_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


@login_required
def post_edit(request, pk):
    print(lineno(), 'request.method =', request.method)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.last_update_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        # request method equals GET
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    print(lineno(), 'request.user =', request.user)
    draft_posts = Post.objects.filter(published_date__isnull=True).filter(author=request.user).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'draft_posts': draft_posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)


@login_required
def post_unpublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.unpublish()
    return redirect('blog.views.post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')


@login_required
def post_encrypt(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(lineno(), 'request.method =', request.method)
    if request.method == "POST":
        form = EncryptForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.password = password
            # post.published_date = timezone.now()
            post.encrypt()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        # request method equals GET
        post = get_object_or_404(Post, pk=pk)
        form = EncryptForm(instance=post)
    return render(request, 'blog/post_encrypt.html', {'form': form, 'post': post})


@login_required
def post_decrypt(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(lineno(), 'request.method =', request.method)
    if request.method == "POST":
        form = DecryptForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.decrypt()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        post = get_object_or_404(Post, pk=pk)
        form = DecryptForm(instance=post)
    return render(request, 'blog/post_decrypt.html', {'form': form, 'post': post})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def post_email(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # email = get_object_or_404(EmailMessage, pk=pk)
    # post = get_object_or_404(Post, pk=pk)
    print(lineno(), 'blog/views post_email request.method =', request.method, 'request = ', request)
    if request.method == "POST":
        form = EmailMessageForm(request.POST)
        if form.is_valid():
            emailmessage = form.save(commit=False)
            emailmessage.post = post
            # emailmessage.destin_email = request.destin_email
            print('emailmessage.destin_email =', emailmessage.destin_email)
            # , 'request.destin_email =', request.destin_email)
            emailmessage.subject = post.title
            # post = form.save(commit=False)
            emailmessage.sender = request.user
            # post.password = password
            # post.published_date = timezone.now()
            emailmessage.send()
            emailmessage.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        # request method equals GET
        post = get_object_or_404(Post, pk=pk)
        form = EmailMessageForm(instance=post)
    return render(request, 'blog/post_email.html', {'form': form, 'post': post})

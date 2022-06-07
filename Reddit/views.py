from django.shortcuts import render, redirect

from .models import Subreddit, Post, Comment
from .forms import SubredditForm, PostForm, CommentForm, EditPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """The home page for Reddit"""
    return render(request, 'Reddit/index.html')


def subreddits(request):
    """Show all subredits"""
    subreddit = Subreddit.objects.order_by('name')
    context = {'subreddit': subreddit}
    return render(request, 'Reddit/subreddits.html', context)


def subreddit(request, subreddit_name):
    """Main subreddit view"""
    name = Subreddit.objects.get(name=subreddit_name)
    all_events = Post.objects.filter(subreddit=name)
    context = {'all_events': all_events,
               'name': name}
    return render(request, 'Reddit/subreddit.html', context)


def post(request, subreddit_name, random_url, slug):
    """Post view"""
    name = Subreddit.objects.get(name=subreddit_name)
    random_url = Post.objects.get(random_url=random_url)
    slug = Post.objects.filter(slug=slug)
    title = random_url.title
    post = random_url.post
    image = random_url.image
    queryset = Comment.objects.filter(post=random_url)

    context = {'name': name,
               'random_url': random_url,
               'slug': slug,
               'title': title,
               'post': post,
               'image': image,
               'object_list': queryset, }

    return render(request, 'Reddit/post.html', context)

@login_required
def new_subreddit(request):
    """Add new subreddit"""
    if request.method != 'POST':
        # Create a blank form
        form = SubredditForm()
    else:
        # process data
        form = SubredditForm(data=request.POST)
        if form.is_valid():
            new_subreddit = form.save(commit=False)
            new_subreddit.owner = request.user
            new_subreddit.save()
            return redirect('Reddit:subreddits')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'Reddit/new_subreddit.html', context)

@login_required
def new_post(request, subreddit_name):
    """Add new post to a subreddit"""
    subreddit = Subreddit.objects.get(name=subreddit_name)

    if request.method != 'POST':
        # Create a blank form
        form = PostForm()
    else:
        # process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.subreddit = subreddit
            new_post.owner = request.user
            new_post.save()
            return redirect('Reddit:subreddit', subreddit_name=subreddit_name)

    # Display a blank or invalid form
    context = {'subreddit': subreddit,
               'form': form}
    return render(request, 'Reddit/new_post.html', context)

@login_required
def new_comment(request, subreddit_name, random_url, slug):
    """Add new comment to a post"""
    subreddit = Subreddit.objects.get(name=subreddit_name)
    url = Post.objects.get(random_url=random_url)
    slugn = Post.objects.filter(slug=slug)

    if request.method != 'POST':
        # Create a blank form
        form = CommentForm()
    else:
        # Process data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = url
            new_comment.owner = request.user
            new_comment.save()
            return redirect('Reddit:post', subreddit_name=subreddit_name, random_url=random_url, slug=slug)

    # Display a blank or invalid form
    context = {'subreddit': subreddit,
               'random_url': url,
               'slug': slugn,
               'form': form}
    return render(request, 'Reddit/new_comment.html', context)

@login_required
def edit_post(request, subreddit_name, random_url, slug):
    """Edit existing Post"""
    name = Subreddit.objects.get(name=subreddit_name)
    random_url = Post.objects.get(random_url=random_url)
    slugn = Post.objects.filter(slug=slug)
    title = random_url.title
    post = random_url.post

    if random_url.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre fill form with the current entry.
        form = EditPostForm(instance=random_url)
    else:
        # POST data submitted; process data
        form = EditPostForm(instance=random_url, data=request.POST)
        if form.is_valid():
            editted_post = form.save(commit=False)
            editted_post.is_edited = True
            editted_post.save()
            return redirect('Reddit:post', subreddit_name=subreddit_name, random_url=random_url.random_url, slug=slug)

    context = {'name': name,
               'random_url': random_url,
               'slugn': slugn,
               'title': title,
               'post': post,
               'form': form}
    return render(request, 'Reddit/edit_post.html', context)

@login_required
def edit_comment(request, subreddit_name, random_url, slug, temporary_key):
    """Edit existing Comment"""
    # Doesn't work right now, rework after adding user auth.
    name = Subreddit.objects.get(name=subreddit_name)
    random_url = Post.objects.get(random_url=random_url)
    slugn = Post.objects.filter(slug=slug)
    key = Comment.objects.get(temporary_key=temporary_key)

    if random_url.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre fill form with the current entry.
        form = CommentForm(instance=key)
    else:
        # POST data submitted; process data
        form = CommentForm(instance=key, data=request.POST)
        if form.is_valid():
            eddited_comment = form.save(commit=False)
            eddited_comment.is_edited = key.is_edited = True
            eddited_comment.save()
            return redirect('Reddit:post', subreddit_name=subreddit_name, random_url=random_url.random_url, slug=slug)

    context = {'name': name,
               'random_url': random_url,
               'slugn': slugn,
               'temporary_key': temporary_key,
               'form': form}
    return render(request, 'Reddit/edit_comment.html', context)

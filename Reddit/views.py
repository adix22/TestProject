from django.shortcuts import render, redirect

from .models import Subreddit, Post, Comment
from .forms import SubredditForm, PostForm


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


def new_subreddit(request):
    """Add new subreddit"""
    if request.method != 'POST':
        # Create a blank form
        form = SubredditForm()
    else:
        # process data
        form = SubredditForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Reddit:subreddits')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'Reddit/new_subreddit.html', context)


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
            new_post.save()
            return redirect('Reddit:subreddit', subreddit_name=subreddit_name)

    # Display a blank or invalid form
    context = {'subreddit': subreddit,
               'form': form}
    return render(request, 'Reddit/new_post.html', context)

from django.shortcuts import render

from .models import Subreddit, Post


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
    slug = Post.objects.get(slug=slug)
    title = slug.title
    post = random_url.post
    image = random_url.image

    context = {'name': name,
               'random_url': random_url,
               'slug': slug,
               'title': title,
               'post': post,
               'image': image,}

    return render(request, 'Reddit/post.html', context)

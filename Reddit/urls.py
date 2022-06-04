"""Defines URL pattern for Reddit"""

from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "Reddit"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all subreddits
    path('subreddits/', views.subreddits, name='subreddits'),
    # Main subreddit page
    path('subreddits/<str:subreddit_name>/', views.subreddit, name='subreddit'),
    # Individual post page
    path('subreddits/<str:subreddit_name>/<uuid:random_url>/<slug:slug>', views.post, name='post'),
    # Urls for user added content
    # New subbreddit page
    path('new_subreddit/', views.new_subreddit, name="new_subreddit"),
    # New post page
    path('subreddits/<str:subreddit_name>/new_post/', views.new_post, name="new_post"),
    # New comment page
    path('subreddits/<str:subreddit_name>/<uuid:random_url>/<slug:slug>/new_comment/',
         views.new_comment, name='new_comment'),
    # Edit post.
    path('subreddits/<str:subreddit_name>/<uuid:random_url>/<slug:slug>/edit_post/', views.edit_post, name='edit_post'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

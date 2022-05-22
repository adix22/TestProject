"""Defines URL pattern for Reddit"""

from django.urls import path
from .import views


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

]

from django import forms

from .models import Subreddit, Post, Comment


class SubredditForm(forms.ModelForm):
    class Meta:
        model = Subreddit
        fields = ['name']
        labels = {'name': ''}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'post']
        labels = {'title': 'Title:',
                  'post': 'Post:'}
        widgets = {'title': forms.Textarea(attrs={'cols': 80,
                                                  'rows': 1}),
                   'post': forms.Textarea(attrs={'cols': 80})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': ''}
        widgets = {'comment': forms.Textarea(attrs={'cols': 80,
                                                    'rows': 40})}


class EditPostForm(PostForm):
    class Meta(PostForm.Meta):
        widgets = {'title': forms.Textarea(attrs={'readonly': 'readonly',
                                                  'cols': 80,
                                                  'rows': 1}),
                   'post': forms.Textarea(attrs={'cols': 80})}

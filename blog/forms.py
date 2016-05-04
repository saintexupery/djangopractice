from .models import Post
from .models import Comment
from django import forms

'''
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
'''

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'message']
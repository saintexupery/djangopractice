from .models import Post
from .models import Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']

class CommentForm2(forms.Form):
    author = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        comment = Comment(**self.cleaned_data)
        if commit:
            comment.save()
        return comment

# CommentForm과 CommentFomr2는 완전히 같은 기능을 하는 코드이다.
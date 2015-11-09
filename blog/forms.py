from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class EncryptForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('password',)
        widgets = {'text': forms.HiddenInput()}


class DecryptForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('password',)
        widgets = {'ciphertext': forms.HiddenInput()}

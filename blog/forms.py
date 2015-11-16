from django import forms
from django.utils.translation import ugettext_lazy as _
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
        # save_password = forms.BooleanField(label="Save password? (not recommended)")
        fields = ('password', 'save_password')
        labels = {
            'password': _('Password'),
            'save_password': _(' Save password? (not recommended)'),
        }
        widgets = {'text': forms.HiddenInput()}


class DecryptForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('password',)
        widgets = {'ciphertext': forms.HiddenInput()}

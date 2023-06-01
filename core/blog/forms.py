from django import forms
from .models import Post
# class ContactForm(forms.Form):
#     name = forms.IntegerField()
#     message = forms.CharField(widget=forms.Textarea)
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author', 'title','content', 'status', 'category', 'published_date']
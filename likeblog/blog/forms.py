from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=60)
    description = forms.CharField(max_length=160)
    text = forms.Textarea()
    icon = forms.ImageField()

    class Meta:
        model = Post
        fields = ('title', 'description', 'text', 'icon')

    # def save(self, commit=True):
    #     blog_post = Post()
    #     blog_post.title = self.changed_data['title']
    #     blog_post.description = self.changed_data['description']
    #     blog_post.text = self.changed_data['text']
    #     if self.changed_data['icon']:
    #         blog_post.icon = self.changed_data['icon']
    #
    #     if commit:
    #         blog_post.save()
    #     return blog_post

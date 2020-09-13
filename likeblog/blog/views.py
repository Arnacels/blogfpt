from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Theme, Post
from .forms import PostForm


# Create your views here.
def start(request):
    contact_list = Theme.objects.all()

    return render(request, 'blog/theme_list.html', {'list': contact_list})


class ThemeView(ListView):
    model = Theme
    paginate_by = 5
    template_name = 'blog/theme_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context, **kwargs)
        context['posts'] = Post.objects.all().order_by('-views')
        return context


class PostView(ListView):
    model = Theme
    paginate_by = 5
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        queryset = Theme.objects.all()
        pk = self.kwargs.get('pk', None)
        print(queryset.get(pk=pk))
        if pk is not None:
            queryset = queryset.get(pk=pk).posts.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-views')
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        self.object.views += 1
        self.object.save()
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-views')
        return context



class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'description', 'text', 'icon')
    template_name = 'blog/edit_post.html'
    redirect_field_name = 'accounts/login/'

    # def post(self, request, *args, **kwargs):
    #     #form = self.get_form_class()(data=request.POST, files=request.FILES)
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'description', 'text', 'icon')
    template_name = 'blog/edit_post.html'
    redirect_field_name = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        creator = self.get_object().creator
        if creator == request.user or request.user.username == 'admin':
            return super().get(request, *args, **kwargs)
        else:
            return redirect('/')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/edit_post.html'
    redirect_field_name = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        creator = self.get_object().creator
        if creator == request.user or request.user.username == 'admin':
            return super().get(request, *args, **kwargs)
        else:
            return redirect('/')


@login_required(redirect_field_name='/accounts/login/')
def like_post(requests, pk):
    post = Post.objects.get(pk=pk)
    if requests.user not in post.likes_user.all():
        post.likes_user.add(requests.user)
    return HttpResponse(str(post.likes_user.all().count()))
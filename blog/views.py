from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from .models import Blog
from .forms import BlogForm
from django.views.generic import UpdateView
# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.order_by('-blog_date')
    return render(request, 'blogs/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})

@user_passes_test(lambda u: u.is_superuser)
def create_blog_post(request):
    if request.method == 'GET':
        return render(request, 'blogs/createblog.html', {'form': BlogForm()})
    else:
        try:
            form = BlogForm(request.POST)
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('blog:all_blogs')
        except ValueError:
            return render(request, 'blogs/createblog.html',
                          {'form': BlogForm(), 'error': 'One or more fields incorrectly filled out.'})

@user_passes_test(lambda u: u.is_superuser)
def deletepost(request, blog_pk):
    todelete = get_object_or_404(Blog, pk=blog_pk, user=request.user)
    if request.method == 'POST':
        todelete.delete()
        return redirect('blog:all_blogs')


@user_passes_test(lambda u: u.is_superuser)
def editpost(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'GET':
        form = BlogForm(instance=blog)
        return render(request, 'blogs/edit.html', {'blog': blog, 'form': form})
    else:
        try:
            form = BlogForm(request.POST, instance=blog)
            form.save()
            return redirect('blog:all_blogs')
        except ValueError:
            return render(request, 'blogs/all_blogs.html', {'blog': blog, 'form': form, 'error': 'Error'})


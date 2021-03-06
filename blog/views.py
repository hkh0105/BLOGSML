from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from .form import BlogForm
# Create your views here.
def list(request):
    blogs = Blog.objects.all()
    return render(request,'list.html',{'blogs':blogs})

def detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    if request.method == 'POST':
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('list')
    else:
        form = BlogForm()
        return render(request,'new.html', {'form':form})

def create(request):
    new_blog=Blog()
    new_blog.title = request.POST['title']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.datetime.now()
    new_blog.save()
    return redirect('/blog/'+ str(new_blog.id))
def edit(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'edit.html',{'blog':blog})
def update(request,blog_id):
    edit_blog=get_object_or_404(Blog,pk=blog_id)
    edit_blog.title = request.POST['title']
    edit_blog.body = request.POST['body']
    edit_blog.pub_date = timezone.datetime.now()
    edit_blog.save()
    return redirect('/blog/'+ str(edit_blog.id))
def delete(request,blog_id):
    delete_blog = get_object_or_404(Blog,pk=blog_id)
    delete_blog.delete()
    return redirect('list')
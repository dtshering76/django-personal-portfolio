from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('date_posted')
    paginator = Paginator(blogs,4)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)
    return render(request,'blog/all_blogs.html',{'page_obj':page_object})

def posts(request,blog_id):
    post=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/post.html',{'post':post})
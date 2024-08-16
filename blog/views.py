from django.shortcuts import render,get_object_or_404
from .models import Post
from next_prev import next_in_order, prev_in_order

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts':posts}
    return render(request,'blog/index.html',context)

def single_view(request,pid):
    post=get_object_or_404(Post,pk=pid,status=1)
    qs=Post.objects.filter(status=1).order_by("pk")
    next = next_in_order(post,qs=qs)
    if next:
            nx=next
    else: nx=post
    prev = prev_in_order(post,qs=qs)
    if prev:
            pr=prev
    else: pr=post
    post.counted_view += 1
    post.save()
    context={'post':post,'next':nx,'prev':pr}
    return render(request,'blog/blog-single.html',context)
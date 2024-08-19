from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from next_prev import next_in_order, prev_in_order
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def blog_view(request,author_name=None):
    posts = Post.objects.filter(status=True)
    if author_name:
           posts = posts.filter(author__username=author_name)
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
    comment = Comment.objects.filter(post=post.id,)
    context={'post':post,'next':nx,'prev':pr,'comment':comment}
    return render(request,'blog/blog-single.html',context)

def comment_view(request):
        if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.add_message(request,messages.SUCCESS,'Your Email Submitted Successfully')
                        return HttpResponseRedirect('/')
                else: 
                       messages.add_message(request,messages.ERROR,'Your Email Not Submitted') 
                       return HttpResponseRedirect('/')
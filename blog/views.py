from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from next_prev import next_in_order, prev_in_order
from .forms import CommentForm,PostForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



# Create your views here.
def blog_view(request,author_name=None,remove_id=None):
        posts = Post.objects.filter(status=True)
        if author_name:
                posts = posts.filter(author__username=author_name)
        if remove_id:
                form=Post.objects.get(id=remove_id)
                form.delete()
                messages.add_message(request,messages.SUCCESS,f'Post Number {remove_id} deleted')
                return HttpResponseRedirect('/')
        posts=Paginator(posts,6)
        try:
                page_number=request.GET.get('page')
                posts=posts.get_page(page_number)
        except PageNotAnInteger:
                posts=posts.get_page(1)
        except EmptyPage:
                posts=posts.get_page(1)

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
                
def newpost_view(request):
        if request.method == 'POST':
                form = PostForm(request.POST,request.FILES)
                if form.is_valid():
                        imgage = form.cleaned_data.get("image")
                        form.save()
                        messages.add_message(request,messages.SUCCESS,'You Created New Post Successfully')
                        return HttpResponseRedirect('blog')
                else: 
                       messages.add_message(request,messages.ERROR,'New Post Not Created') 
                       return HttpResponseRedirect('blog')
        form = PostForm()
        return render(request,'blog/newpost.html',{'form':form})
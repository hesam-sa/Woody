from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from next_prev import next_in_order, prev_in_order
from .forms import CommentForm,PostForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



# Create your views here.
def blog_view(request,**kwargs):
        posts = Post.objects.filter(status=True)
        filter = ""
        folder = ""
        if kwargs.get('author_name') != None:
                posts = posts.filter(author__username=kwargs['author_name'])
                filter = kwargs['author_name']
                folder = 'author'
        if  kwargs.get('remove_id') != None:
                if request.user.is_authenticated:
                        form=Post.objects.get(id=kwargs['remove_id'])
                        form.delete()
                        messages.add_message(request,messages.SUCCESS,f'Post Number {kwargs["remove_id"]} deleted')
                        return redirect(request.META['HTTP_REFERER'])
                else:
                        messages.add_message(request,messages.ERROR,"You Dont Have Permision To delete A Post")
                        return redirect('/blog')
                
        if kwargs.get('tag_name') != None:
                posts = posts.filter(tags__name=kwargs['tag_name'])
                filter = kwargs['tag_name']            
                folder = 'tag'
        if kwargs.get('cat_name') != None:
                posts = posts.filter(category__name=kwargs['cat_name'])
                filter = kwargs['cat_name']
                folder = 'category'
        posts=Paginator(posts,6)
        try:
                page_number=request.GET.get('page')
                posts=posts.get_page(page_number)
        except PageNotAnInteger:
                posts=posts.get_page(1)
        except EmptyPage:
                posts=posts.get_page(1)

        context = {'posts':posts,'filter':filter,'folder':folder}
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
    if not post.login_required:
        post.counted_view += 1
        post.save()
        comment = Comment.objects.filter(post=post.id,)
        context={'post':post,'next':nx,'prev':pr,'comment':comment}
        return render(request,'blog/blog-single.html',context)
    else:
        if request.user.is_authenticated:
                post.counted_view += 1
                post.save()
                comment = Comment.objects.filter(post=post.id,)
                context={'post':post,'next':nx,'prev':pr,'comment':comment}
                return render(request,'blog/blog-single.html',context)
        else:
                messages.add_message(request,messages.ERROR,'You Should Login First To See This Post')
                return redirect(request.META['HTTP_REFERER'])

def comment_view(request):
        if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.add_message(request,messages.SUCCESS,'Your Comment Submitted Successfully')
                        return redirect(request.META['HTTP_REFERER'])
                else: 
                       messages.add_message(request,messages.ERROR,'Your Email Not Submitted') 
                       return HttpResponseRedirect(request.META['HTTP_REFERER'])
                
def newpost_view(request):
        if request.user.is_authenticated:
                if request.method == 'POST':
                        
                        form = PostForm(request.POST,request.FILES)
                        
                        if form.is_valid():
                                image = form.cleaned_data.get("image")
                                form.save()
                                messages.add_message(request,messages.SUCCESS,'You Created New Post Successfully')
                                return HttpResponseRedirect('/blog')
                        else: 
                                messages.add_message(request,messages.ERROR,'New Post Not Created') 
                                return HttpResponseRedirect(request.META['HTTP_REFERER'])
                form = PostForm()
                user_id=request.user.id
                field = form.fields['author']
                field.initial = user_id
                field.widget = field.hidden_widget()
                return render(request,'blog/newpost.html',{'form':form})
        else:
                messages.add_message(request,messages.ERROR,'For Create New Post You should Login First') 
                return redirect('/blog')
        

def serach_view(request):
        posts = Post.objects.filter(status=1)
        if request.method == 'GET':
                if s := request.GET.get('s'):
                        posts = posts.filter(content__contains = s)

        context = {'posts':posts}
        return render(request,'blog/index.html',context)

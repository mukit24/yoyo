from django.shortcuts import render,redirect,HttpResponse
from .models import Post,React,Comment
from .forms import PostForm,CommentForm,UpdatePostForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def post_view(request):
    post_form = PostForm()
    post_list = Post.objects.all().order_by('-created_on')
    for x in post_list:
        print(x.id)
    if request.method == 'POST':
        try:
            temp = request.user.volunteer
        except:
            return HttpResponse('<h1>Sorry You Dont Have A volunteer Profile</h1><h2>Please Create A volunteer Profile From Your Profile Section</h2>')
        if request.user.is_anonymous:
            return redirect('account_signup')
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = Post(
                body=form.cleaned_data["body"],
                image=form.cleaned_data["image"],
                author=request.user.volunteer,
            )
            post.save()
            return redirect('post_view')

    paginator = Paginator(post_list,5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts':posts,
        'post_form':post_form,
    }
    return render(request,"post/post_view.html",context)

@login_required
def react(request,id):
    post = Post.objects.get(id=id)
    # print(request.user in post.react.all())
    try:
        re = React.objects.get(Q(author=request.user) & Q(post=post))
        re.delete()
    except:
        re = React(
            author=request.user,
            post=post,
        )
        re.save()

    post_form = PostForm()
    post_list = Post.objects.all().order_by('-created_on')
    paginator = Paginator(post_list,5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts':posts,
        'post_form':post_form,
        'anchor':post.id,
    }
    return render(request,"post/post_view.html",context)

@login_required
def react_d(request,id):
    post = Post.objects.get(id=id)
    try:
        re = React.objects.get(Q(author=request.user) & Q(post=post))
        re.delete()
    except:
        re = React(
            author=request.user,
            post=post,
        )
        re.save()
    return redirect('post_details',post.id)


    

def post_details(request,id):
    post = Post.objects.get(id=id)
    cmt_form = CommentForm()
    update_post = UpdatePostForm(instance=post)
    if request.method == 'POST':
        update_post = UpdatePostForm(request.POST,request.FILES, instance=post)
        if update_post.is_valid():
            post.save()
        return redirect('post_details',id=post.id)
    context = {
        'post':post,
        'cmt_form':cmt_form,
        'update_post':update_post,
    }
    return render(request,"post/post_details.html",context)

@login_required
def add_comment(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = Comment(
                author=request.user,
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
        return redirect('post_details',id=post.id)


def delete_post(request,id):
    # print('yoo')
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post_view')


def edit_comment(request,id):
    comment = Comment.objects.get(id=id)
    post_id = comment.post.id
    new_body = request.POST['comment']
    comment.body = new_body
    comment.save()
    return redirect('post_details',id=post_id)


def delete_comment(request,id):
    comment = Comment.objects.get(id=id)
    post_id = comment.post.id
    comment.delete()
    return redirect('post_details',id=post_id)



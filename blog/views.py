from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form":CommentForm()
    }
    if request.method == "POST":
        data = request.POST
        form = CommentForm(data=data)
        if form.is_valid():
            # Comment.objects.create(author = data['author'], body=data['body'], post=post)
            form.save()
            # instance.post = post
            # instance.save()

        else:
            return render(request, "blog/detail.html", context)

    return render(request, "blog/detail.html", context)
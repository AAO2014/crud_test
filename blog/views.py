from celery import shared_task
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from blog.models import Post


@shared_task
def image_save(filename_in, filename_out):
    print
    file = open(filename_in, 'r')
    file.write(filename_out)


def index(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts})


def create(request):
    if request.method == "POST":
        filename = request.POST.get("image")
        newpost = Post(
            title=request.POST.get("title"),
            text=request.POST.get("text"),
            image=filename
        )
        newpost.save()
        # image_save.delay(filename, newpost.image.path)
    return HttpResponseRedirect("/blog/")


def edit(request, id):
    try:
        post = Post.objects.get(id=id)

        if request.method == "POST":
            post.title = request.POST.get("title")
            post.text = request.POST.get("text")
            post.save()
            return HttpResponseRedirect("/blog/")
        else:
            return render(request, "edit.html", {"post": post})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/blog/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")
# from django.shortcuts import render
from typing import Any

from django.http import Http404, HttpRequest
from django.shortcuts import render

from blog.data import posts

# Create your views here.
context = {
    # 'text': 'Estamos no Blog agora',
    'title': 'Blog do ',
    'posts': posts
}


def blog(request):
    return render(request,
                  'blog/index.html',
                  context
                  )


def post(request: HttpRequest, post_id):
    found_post: dict[str, Any] | None = None
    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')

    context = {
        'post': found_post
    }

    return render(request,
                  'blog/post.html',
                  context
                  )

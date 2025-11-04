from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
import logging

logger = logging.getLogger(__name__)

def index(request):
  posts = ["ASD","asdas"]
  logger.debug("Got %d posts", len(posts))
  return render(request, "blog/index.html")

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  
  logger.info(
      "Created comment on Post %d for user %s", post.pk, request.user
  )
  return render(request, "blog/post-detail.html", {"post": post})
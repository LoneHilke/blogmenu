from django.urls import path
from neapolitan.views import CRUDView
from .models import Post


class BookmarkView(CRUDView):
    model = Post
    fields = ["title", "content"]

urlpatterns = [
    *BookmarkView.get_urls(),
]
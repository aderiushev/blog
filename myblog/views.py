from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-ts')
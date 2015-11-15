from django.views import generic
from .models import Post


class ResumeView(generic.TemplateView):
    template_name = 'myblog/resume.html'


class BlogView(generic.ListView):
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-ts')


class PostView(generic.DetailView):
    model = Post

    def get_object(self, queryset=None):
        return Post.objects.get(slug=self.kwargs['slug'])


class IndexView(generic.TemplateView):
    template_name = 'myblog/index.html'

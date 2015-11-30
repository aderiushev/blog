from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^blog/post/(?P<slug>[a-z-]+)$', views.PostView.as_view(), name='blog-post'),
    url(r'^resume/$', views.ResumeView.as_view(), name='resume'),
    url(r'^portfolio/$', views.PortfolioView.as_view(), name='portfolio')
]
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .models import Post


def indexView(request):
    return render(request, 'index.html', {'name':'Hasan'} )
class IndexView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        #super idicate to parrent class (TemplateView)
        context["name"] = 'Omid'
        context["posts"]=Post.objects.all()
        return context
    
class RedirectToVmusic(RedirectView):
    url='https://discogs.vmusic.ir/'
    '''def get_redirect_url(self, *args, **kwargs):
        post=get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)'''
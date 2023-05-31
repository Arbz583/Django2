from django.shortcuts import render
from django.views.generic import TemplateView
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
    
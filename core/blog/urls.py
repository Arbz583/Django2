from django.urls import path
from .import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name='blog'

urlpatterns = [
    path('fbv-index', views.indexView, name='fbv-index'),
    #path('cbv-index', TemplateView.as_view(template_name="index.html",extra_context={'name':'ali'})),
    path('cbv-index', views.IndexView.as_view(), name='cbv-index' ),
    path('go-to-django/', RedirectView.as_view(url='https://www.djangoproject.com/')),
    path('go-to-index/', RedirectView.as_view(pattern_name='blog:cbv-index'), ),
    path('go-to-vmusic/<int:pk>/', views.RedirectToVmusic.as_view(),name='redirect to vmusic'), #to change your url! also passing paras in optional.
    path('post/', views.PostList.as_view(), name='post-list')
    
]

    

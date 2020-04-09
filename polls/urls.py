from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rel', views.rel, name='rel'),
    path('rel/insert', views.insert, name='insert'),
    path('rel/find', views.find, name='find'),
    path('rel/delete', views.delete, name='delete'),
    path('rel/update', views.update, name='update'),   
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
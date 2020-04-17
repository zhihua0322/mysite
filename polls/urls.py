from django.urls import path

from . import views
from . import forms

app_name = 'polls'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('departments', views.DepartmentsListView.as_view(), name='departments'), 
    path('departments/<int:pk>', views.DepartmentsDetailView.as_view(), name='departments_detail'),
    path('departments/create', views.DepartmentsCreateView.as_view(), name='departments_create'),
    path('departments/delete/<int:pk>', views.DepartmentsDeleteView.as_view(), name='departments_delete'),
    path('departments/update/<int:pk>', views.DepartmentsUpdateView.as_view(), name='departments_update'),
    path('rel', views.rel, name='rel'),
    path('rel/insert', views.insert, name='insert'),
    path('rel/find', views.find, name='find'),
    path('rel/delete', views.delete, name='delete'),
    path('rel/update', views.update, name='update'),
    path('rel/building', views.building, name='building'),   
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
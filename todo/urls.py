from django.urls import path,include
from .views  import TodoListView, TodoDetailView, CompletedListView, TodoCreateView

app_name= 'todo'

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('completed/', CompletedListView.as_view(), name='completed_list'),
    path('detail/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('new/', TodoCreateView.as_view(), name='new'),
]
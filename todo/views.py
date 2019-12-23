from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Tag, Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todo_list'

    def Token(request):
        ctxt = RequestContext(request, {})
        return render_to_response("todo_list.html", ctxt)

class CompletedListView(ListView):
    model = Todo
    template_name = 'completed_list.html'
    context_object_name = 'completed_list'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail_list.html'
    context_object_name = 'todo_detail'

class TodoCreateView(CreateView):
    model = Todo
    template_name= 'todo_form.html'
    fields = ['title','tag','body','due_date']
